# Project Roadmap

## Day 1 — Foundation
### Objectives
- Set up GitHub repository and project structure
- Prepare synthetic dataset
- Configure Databricks Community Edition
- Build Bronze ingestion pipeline

### Completed
- Created GitHub repo and folder structure
- Added raw dataset (transactions.csv)
- Added synthetic data generator (transaction.py)
- Created Unity Catalog Volume (bronze_volume)
- Built Bronze ingestion notebook (PySpark → Delta Lake)
- Exported notebook to GitHub
- Added Bronze section + architecture diagram to README
- Created 'ROADMAP.md'

---

## Day 2 — Silver & Gold Layers
### Objectives
- Build Silver transformation logic
- Create Silver Delta Lake table
- Add Silver to GitHub
- Update README with Silver & Gold sections

### Completed
- Defined Silver transformation rules (cleaning, hashing, standardization)
- Created Silver notebook in Databricks
- Applied Silver transformations (clean, standardize, hash, derive fields)
- Wrote Silver Delta table
- Exported Silver notebook to Github
- Updated README with Silver Layer

### Planned Tasks
- Clean and aggregated metrics (Gold)
- Add business logic transformations (Gold)
- Write Gold Delta tables
- Export Gold notebooks to Github
- Update README with Gold Section
- Add business logic transformations (Silver)
- Create aggregated metrics (Gold)
- Write Silver and Gold Delta tables
- Export notebooks to GitHub
- Update documentation

---

## Future Enhancements
### Objectives
- Add orchestration, quality checks, and visualization

### Planned Tasks
- Add Airflow or Databricks Jobs pipeline
- Add data quality checks (Great Expectations or custom)
- Add dashboard (Power BI, Databricks SQL, or Tableau)
- Add unit tests for transformations
- Add CI/CD (GitHub Actions)
- Add monitoring & logging
