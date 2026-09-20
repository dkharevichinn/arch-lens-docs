# Arch Lens catalog site

Public MkDocs Material catalog of every finding, metric, and gate verdict Arch Lens emits.

This repository is a flattened copy of `docs/site/` from [`dkharevichinn/arch-lens`](https://github.com/dkharevichinn/arch-lens) `main`. It does **not** include `docs/superpowers/`.

Stable URLs (GitHub Pages, Actions):

- Finding code `A1` → https://dkharevichinn.github.io/arch-lens-docs/findings/A1/
- Metric key `tanglePct` → https://dkharevichinn.github.io/arch-lens-docs/metrics/tanglePct/
- Gate verdict `block` → https://dkharevichinn.github.io/arch-lens-docs/gates/block/

Build locally:

```bash
pip install -r requirements.txt
mkdocs serve
```

The GitHub Actions workflow `.github/workflows/pages.yml` builds with `mkdocs build --strict` and deploys from `main`. See [enable Pages](docs/enable-pages.md).
