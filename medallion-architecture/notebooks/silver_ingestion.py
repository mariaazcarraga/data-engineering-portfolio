# Databricks notebook source
# Read the bronze table

df_bronze = spark.read.format("delta").load("/Volumes/workspace/default/bronze_volume/bronze_transactions")
df_bronze.show()

# Convert transaction_date to proper date
from pyspark.sql.functions import to_date, col

df_silver = df_bronze.withColumn("transaction_date", to_date(col("transaction_date")))

# Remove duplicates
df_silver = df_silver.dropDuplicates(["transaction_id"])

# Normalize text fields
from pyspark.sql.functions import trim, lower

df_silver = df_silver.withColumn("country", trim(col("country")))
df_silver = df_silver.withColumn("channel", trim(col("channel")))
df_silver = df_silver.withColumn("merchant_category", trim(col("merchant_category")))
df_silver = df_silver.withColumn("status", trim(col("status")))

# Hash sensitive fields
from pyspark.sql.functions import sha2

df_silver = df_silver.withColumn("customer_id_hash", sha2(col("customer_id").cast("string"), 256))
df_silver = df_silver.withColumn("transaction_id_hash", sha2(col("transaction_id").cast("string"), 256))

# Drop raw identifiers
df_silver = df_silver.drop("customer_id", "transaction_id")

# Add derived fields
from pyspark.sql.functions import year, month, dayofmonth

df_silver = df_silver.withColumn("year", year("transaction_date"))
df_silver = df_silver.withColumn("month", month("transaction_date"))
df_silver = df_silver.withColumn("day", dayofmonth("transaction_date"))

# COMMAND ----------

# Save it to volume

df_silver.write.format("delta").mode("overwrite").save("/Volumes/workspace/default/bronze_volume/silver_transactions")
