from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ClaimsETL").getOrCreate()

df = spark.read.csv("s3://claims-raw-data/", header=True)

df_valid = df.filter(df.ClaimAmount > 0)

df_valid.write.mode("overwrite").parquet("s3://claims-processed/accepted/")
