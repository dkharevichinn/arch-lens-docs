# Public catalog origin

GitHub Free cannot publish Pages from this **private** product repo. The operator catalog is copied to the public repo [`dkharevichinn/arch-lens-docs`](https://github.com/dkharevichinn/arch-lens-docs) and served at [https://dkharevichinn.github.io/arch-lens-docs/](https://dkharevichinn.github.io/arch-lens-docs/).

`CatalogConsistencyTests` in this repo still requires every product finding code and `metrics.json` key to have a page under `docs/site/docs/`. Keep `docs/site/product-codes.json` in sync when adding a code; the public repo CI checks the same file against Markdown pages.

## Publish copy (public repo)

Do not copy `docs/superpowers/`. From this product repo:

```bash
rsync -a --delete docs/site/docs/ "$DEST/docs/"
cp docs/site/mkdocs.yml docs/site/requirements.txt \
   docs/site/product-codes.json docs/site/check-catalog-pages.py "$DEST/"
```

`$DEST` is a clone of `dkharevichinn/arch-lens-docs`. Pages uses GitHub Actions (`mkdocs build --strict` + `check-catalog-pages.py`).

## Local preview

```bash
cd docs/site
pip install -r requirements.txt
mkdocs serve
```

Do not publish `docs/superpowers/` as the Pages root. That tree is design history in git; this site is the operator catalog.
