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
- Created Unity Catalog Volume (bronze_volume)
- Built Bronze ingestion notebook (PySpark → Delta Lake)
- Exported notebook to GitHub
- Added Bronze section + architecture diagram to README
- Created ROADMAP.md

---

## Day 2 — Silver & Gold Layers
### Objectives
- Build Silver transformation logic
- Build Gold aggregation logic
- Create Delta Lake tables for both layers
- Add Silver and Gold notebooks to GitHub
- Update README with Silver & Gold sections

### Planned Tasks
- Clean and standardize Bronze data (Silver)
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
