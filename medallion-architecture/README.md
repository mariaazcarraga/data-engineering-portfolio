## Problem

Raw transactional data is messy, inconsistent, and difficult to analyze. It contains mixed currencies, multiple countries, inconsistent formats, and various transaction statuses. Business teams cannot build reliable dashboards or KPIs directly from raw data.

## Solution

This project implements the Medallion Architecture (Bronze -> Silver -> Gold) using PySpark and Delta Lake.

- **Bronze** stores raw data exactly as it is received.
- **Silver** cleans, validates, hashes and standardizes the data.
- **Gold** produces business-ready tables and KPIs for analytics.

This layered approach ensures:
- Reproducible pipelines
- Clean and trustworthy data
- Scalable analytics
- Scalable analytics
- Clear separation of concerns

## Bronze Layer

The Bronze layer ingests raw CSV data (`transactions.csv`) stored in Unity Catalog Volumes and writes it into Delta Lake as the first stage of the Medallion Architecture.

The `transactions.csv` file is a synthetic dataset generated using a Python script that produces randomized transaction data for testing and development.

### Steps performed
- Read raw CSV using PySpark from Unity Catalog Volumes
- Display raw data for validation
- Write the dataset as a Delta Lake table into the Bronze Volume

## Silver Layer

The silver layer will clean, validate, stardize, and hash sensitive fields from the Bronze dataset.

### Steps performed
- Converted transaction_date to proper date type
- Removed duplicates
- Normalized text fields
- Hashed customer_id and transaction_id
- Added derived fields (year, month, day)
- Wrote Silver Delta table

## Gold Layer

The Gold layer will produce business-ready tables and KPIs for analytics and dashboards.

This includes:
- Aggregations
- KPI calculations
- Joins across Silver tables
- Dashboard-ready output tables

### Notebook
- `notebooks/bronze_ingestion.ipynb`
- `notebooks/silver_ingestion.ipynb`
- `notebooks/gold_ingestion.ipynb`

---

### Architecture Diagram
Raw Data → Bronze → Silver → Gold → Dashboard
