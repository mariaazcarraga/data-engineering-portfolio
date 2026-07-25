## Bronze Layer

The Bronze layer ingests raw CSV data (`transactions.csv`) stored in Unity Catalog Volumes and writes it into Delta Lake as the first stage of the Medallion Architecture.

The `transactions.csv` file is a synthetic dataset generated using a Python script that produces randomized transaction data for testing and development.

### Steps performed
- Read raw CSV using PySpark from Unity Catalog Volumes
- Display raw data for validation
- Write the dataset as a Delta Lake table into the Bronze Volume

### Notebook
- `notebooks/bronze_ingestion.ipynb`
