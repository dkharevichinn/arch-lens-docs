# Metrics — метрики

Страницы метрик названы **ключами файла `metrics.json`** (`tanglePct`, `coreSize`, `runtime` и так далее), и адрес каждой — `/metrics/{ключ}/`. Чипы и заголовки таблиц на вкладке Metrics отчёта ведут на эти же страницы: соответствие «подпись в отчёте → ключ» зашито в `DocsCatalog` продукта и дублируется HTML-комментариями на страницах, чтобы автотест `CatalogConsistencyTests` мог проверить, что каждый чип и каждая таблица привязаны ровно к одной странице.

Все метрики считаются в `StaticMetricsCalculator.Calculate` по [графу модулей](../glossary.md#module-graph), то есть только по [учитываемым модулям](../glossary.md#scored): сборки с ролями `host` и `test` в них не входят. Единственное исключение — [`testsPastContract`](testsPastContract.md), для которой тестовые сборки служат источником рёбер. Чипы в шапке отчёта на вкладке Matrix (`components`, `dependencies`, `weight`, `cycles`, `findings`, `contracts`, `language`, `generated`, `commit`) относятся к самому отчёту и матрице компонентов, а не к графу модулей, поэтому страниц для них нет; в частности, чип `cycles` считает циклы между компонентами матрицы и не совпадает с разделом Cycles вкладки Metrics.

## Чипы вкладки Metrics

Чипы выводятся в этом порядке. Дробные метрики хранятся в JSON как доли от 0 до 1, а на чипе показываются в процентах с округлением до двух знаков; `propagation` показывается с тремя знаками после точки; медианы могут быть половинными.

| Чип | Ключ `metrics.json` | Что это одной фразой | Порог гейта |
|---|---|---|---|
| `tangle` | [`tanglePct`](tanglePct.md) | доля межмодульного веса внутри циклических групп модулей | [B2](../findings/B2.md) |
| `feedback` | [`feedbackWeight`](feedbackWeight.md) | суммарный вес рёбер, направленных против вычисленного порядка слоёв | [B3](../findings/B3.md) |
| `propagation` | [`propagationCost`](propagationCost.md) | средняя доля модулей, до которых можно добраться из одного модуля по зависимостям | [B4](../findings/B4.md) |
| `shared gravity` | [`sharedGravity`](sharedGravity.md) | доля межмодульного веса, направленного в модули с ролью `shared` | [B9](../findings/B9.md) |
| `shared types` | [`sharedTypeCount`](sharedTypeCount.md) | число типов в сборках с ролью `shared` | нет |
| `median types` | [`medianTypes`](medianTypes.md) | медиана числа типов по модулям | нет; масштаб для [C1](../findings/C1.md) |
| `max types` | [`maxTypes`](maxTypes.md) | наибольшее число типов в одном модуле | нет |
| `median loc` | [`medianLoc`](medianLoc.md) | медиана строк кода по модулям | нет |
| `max loc` | [`maxLoc`](maxLoc.md) | наибольшее число строк кода в одном модуле | нет |
| `coreShare` | [`coreShare`](coreShare.md) | доля модулей, входящих в наибольшую циклическую группу | нет |
| `coreSize` | [`coreSize`](coreSize.md) | число модулей в наибольшей циклической группе | [B5](../findings/B5.md) (`trigger`) |
| `maxModulePath` | [`maxModulePath`](maxModulePath.md) | длина самой длинной цепочки модулей в рёбрах | [B6](../findings/B6.md) (`trigger`) |
| `testsPastContract` | [`testsPastContract`](testsPastContract.md) | доля тестовых связей, идущих в реализацию, инфраструктуру или UI мимо контракта и `shared` | [F1](../findings/F1.md) |

## Таблицы вкладки Metrics

| Заголовок в отчёте | Ключ `metrics.json` | Что в таблице | Связанные правила |
|---|---|---|---|
| Cycles | [`cycles`](cycles.md) | список циклических групп модулей или надпись `no module cycles` | [B1](../findings/B1.md), [B5](../findings/B5.md) |
| Runtime (DI) | [`runtime`](runtime.md) | счётчики регистраций, портов и рёбер `binding`; список циклов с учётом DI или надпись `no runtime cycles` | [R1](../findings/R1.md), [R2](../findings/R2.md) |
| Modules | [`moduleSize`](moduleSize.md) | по модулю: типы, строки кода, а также колонки Fan-in, Fan-out и Public impl из других ключей | [C1](../findings/C1.md), [C4](../findings/C4.md), [P3](../findings/P3.md), [B7](../findings/B7.md), [A3](../findings/A3.md) |
| Contracts | [`contractSurface`](contractSurface.md) | по контрактной сборке (колонка Unit): публичная поверхность (колонка Surface) | [A4](../findings/A4.md), [A8](../findings/A8.md), [G2](../findings/G2.md) |
| Martin | [`martin`](martin.md) | по модулю: `instable`, `abstractness`, `distance`, `afferent`, `efferent` | [B8](../findings/B8.md) |
| Cohesion | [`cohesion`](cohesion.md) | по модулю с четырьмя и более типами: `h`, `islands` | [D1](../findings/D1.md), [D2](../findings/D2.md) |
| Layer LOC | [`layerLoc`](layerLoc.md) | по модулю: строки кода в сборках `contract`, `implementation`, `infrastructure`, `ui` | [C2](../findings/C2.md), [C3](../findings/C3.md) |

Таблицы Martin, Cohesion и Layer LOC не выводятся, если соответствующий словарь пуст (например, в решении нет модуля с четырьмя типами — не будет таблицы Cohesion).

## Ключи без собственного чипа или таблицы

| Ключ `metrics.json` | Где виден в отчёте | Правило |
|---|---|---|
| [`fanInOut`](fanInOut.md) | колонки Fan-in и Fan-out таблицы Modules | [B7](../findings/B7.md), [P3](../findings/P3.md), через `afferent`/`efferent` — [B8](../findings/B8.md) |
| [`publicInImplementation`](publicInImplementation.md) | колонка Public impl таблицы Modules | [A3](../findings/A3.md) |

Заголовки с именами модулей между таблицами Contracts и Martin — это каталог модулей (`snapshot.Modules.Groups`): перечень сборок каждого модуля с их ролями. Он показывает, как YAML и конвенции разложили сборки по модулям и ролям, и ключом `metrics.json` не является.

## Какие метрики являются порогами

Семь значений копируются командой `arch-lens baseline` в `baseline.ratchets` и затем сравниваются гейтом строгим «больше»: `publicInImplementation` (по модулям), `contractSurface` (по сборкам), `tanglePct`, `feedbackWeight`, `propagationCost`, `sharedGravity`, `testsPastContract`. Остальные метрики — диагностические: они либо служат входом для правил класса `trigger` (`cycles`, `coreSize`, `maxModulePath`, `medianTypes`, `martin`, `cohesion`, `layerLoc`, `fanInOut`, `runtime`), либо просто показывают масштаб (`sharedTypeCount`, `maxTypes`, `medianLoc`, `maxLoc`, `coreShare`, `moduleSize`). Подробно о порогах — в словаре, раздел [ratchet](../glossary.md#ratchet).
