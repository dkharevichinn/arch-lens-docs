# moduleSize

<!-- report-table: Modules -->

| Поле | Значение |
|---|---|
| Ключ в `metrics.json` | `moduleSize` (объект: идентификатор модуля → `{ "types": целое, "loc": целое }`); в коде это свойство `StaticMetrics.ModuleSizes` |
| Таблица на вкладке Metrics | **Modules** с колонками `Module | Types | LOC | Fan-in | Fan-out | Public impl`; первые две числовые колонки берутся из `moduleSize`, остальные — из [fanInOut](fanInOut.md) и [publicInImplementation](publicInImplementation.md) |
| Где считается | `StaticMetricsCalculator.Calculate`: цикл по `snapshot.Code.Types` |
| Порог / связанные правила | порога в `baseline.json` нет; по этим числам работают [C1](../findings/C1.md) (выброс по типам), [P3](../findings/P3.md) (мёртвый модуль при `types > 0`) и, с `--against`, [C4](../findings/C4.md) (прирост типов); из них же выводятся чипы [medianTypes](medianTypes.md), [maxTypes](maxTypes.md), [medianLoc](medianLoc.md), [maxLoc](maxLoc.md) |

## Термины

**Модуль** ([словарь](../glossary.md#module)) — группа сборок с одним идентификатором: обычно `X.Contracts` и `X`, иногда ещё `X.Infrastructure` и `X.UI`. Размер считается по модулю целиком, поэтому контрактные типы входят в `types` наравне с типами реализации.

**Учитываемый модуль** ([словарь](../glossary.md#scored)) — модуль, сборки которого имеют роль, отличную от `host` и `test`. Ключи объекта `moduleSize` — это модули из `graph.Modules`, то есть учитываемые модули, у которых есть хотя бы один тип; тестовые сборки модуля `X` (`X.Tests`) в его размер не входят.

**Тип** — любое именованное объявление, извлечённое из исходного кода: класс, интерфейс, структура, перечисление, делегат, запись, каждый вложенный тип отдельно, независимо от доступности. Типы, объявленные только в сгенерированных файлах (`*.g.cs`, `*.g.i.cs`, `*.generated.cs`), не извлекаются. **LOC** ([словарь](../glossary.md#loc)) — физические строки объявления типа, суммарно по `partial`-частям, без сгенерированных частей.

## Что измеряет

Объект отвечает на вопрос: **сколько типов и сколько строк содержит каждый учитываемый модуль**.

```text
для каждого m из graph.Modules:            moduleSize[m] = { types: 0, loc: 0 }
для каждого типа t из snapshot.Code.Types:
  роль сборки t ∈ { host, test }            → тип пропускается
  m = модуль сборки t
  moduleSize[m].types += 1
  moduleSize[m].loc   += t.Loc
```

Пример из юнит-теста `C1_median_and_max_of_per_module_sizes`: модуль `Small` с одним типом на одну строку и модуль `Big` с тремя типами по одной строке дают `moduleSize = { "Big": { "types": 3, "loc": 3 }, "Small": { "types": 1, "loc": 1 } }`. Ключи упорядочены по ordinal, как и строки таблицы Modules.

## Как читать

- **Таблица Modules — сводная.** Колонки Types и LOC — это `moduleSize`; Fan-in и Fan-out — число модулей-зависимых и модулей-зависимостей из `fanInOut`; Public impl — число публичных типов в сборках реализации и инфраструктуры из `publicInImplementation`. Заголовки Modules, Fan-in, Fan-out и Public impl — ссылки на страницы каталога. Строки идут по имени модуля, а не по размеру; целые числа выводятся с разделителем тысяч (`12,480`).
- **В JSON только размеры.** Объект `moduleSize` содержит `types` и `loc`; остальные колонки таблицы лежат в отдельных ключах `fanInOut` и `publicInImplementation`.
- **Размер включает контракт.** Модуль из 6 контрактных и 30 реализационных типов показывает `types: 36`. Разбивку по ролям инструмент даёт только для строк — таблица Layer LOC и ключ [layerLoc](layerLoc.md); для типов такой разбивки в отчёте нет, хотя правило [C2](../findings/C2.md) считает её внутри себя.
- **Типы и строки расходятся осмысленно.** Много типов при малом LOC — модуль из DTO, перечислений и записей; мало типов при большом LOC — несколько толстых классов. Отношение `loc / types` строки таблицы — средний размер типа в модуле.
- **Медианы и максимумы** по колонкам Types и LOC — чипы `median types`, `max types`, `median loc`, `max loc` над таблицей; их страницы объясняют, почему в качестве масштаба взята медиана.
- **Где искать.** Таблица Modules на вкладке Metrics; объект `moduleSize` в `metrics.json`. В `baseline.json` размеров нет: гейт их не сравнивает.

## Что считать плохим

- **Строка с `Types >= 20`, где число типов не меньше `3 × medianTypes`** — находка [C1](../findings/C1.md) класса `trigger` с сообщением `size outlier: {module}`.
- **Строка с `Types > 0`, `Fan-in = 0` и `Fan-out = 0`** — модуль, который ни от кого не зависит и никому не нужен: находка [P3](../findings/P3.md) с сообщением `dead module: {module}`. Зависимости из `host` и `test` в fan-in не входят, поэтому модуль, который подключает только корень композиции, тоже попадёт сюда.
- **Строка, растущая быстрее остальных.** При `gate --against old-graph.json` правило [C4](../findings/C4.md) отмечает модуль, взявший 70 % и более положительного прироста типов при собственном приросте от 5 типов.
- **Строка, где Public impl приближается к Types**, — сборки реализации, в которых всё публично; это предмет [A3](../findings/A3.md) и страницы [publicInImplementation](publicInImplementation.md).
- **При четырёх и более модулях строка с `Fan-out = N − 1`** либо с `Fan-in = N − 1` без контрактной сборки и не `shared` — выброс по связям, находка [B7](../findings/B7.md).

См. также [medianTypes](medianTypes.md), [maxTypes](maxTypes.md), [medianLoc](medianLoc.md), [maxLoc](maxLoc.md), [fanInOut](fanInOut.md), [publicInImplementation](publicInImplementation.md), [layerLoc](layerLoc.md), [C1](../findings/C1.md), [C4](../findings/C4.md), [P3](../findings/P3.md).
