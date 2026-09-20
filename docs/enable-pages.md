# Enable GitHub Pages

This repository is **public**. Catalog sources sit at the repo root (flattened from product `docs/site/`) and build with MkDocs Material. A workflow (`.github/workflows/pages.yml`) deploys on push to `main`.

## Dashboard click

1. Open [github.com/dkharevichinn/arch-lens-docs](https://github.com/dkharevichinn/arch-lens-docs).
2. **Settings** → **Pages**.
3. Under **Build and deployment** → **Source**, choose **GitHub Actions** (not “Deploy from a branch”).
4. Save if the UI shows a save control.
5. Re-run the **GitHub Pages** workflow from the **Actions** tab, or push an empty commit to `main`, if the first deploy was skipped because Pages was off.
6. Expected site URL: [https://dkharevichinn.github.io/arch-lens-docs/](https://dkharevichinn.github.io/arch-lens-docs/).

## Local preview

```bash
pip install -r requirements.txt
mkdocs serve
```

Do not publish product `docs/superpowers/` as the Pages root. That tree is design history in the private product repo; this site is the operator catalog.
