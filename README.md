#  Insurance Claims Processing Pipeline

# Overview
Serverless ETL pipeline to process insurance claims using AWS services.

# Architecture
1. Data uploaded to S3
2. Lambda validates claims
3. Accepted → RDS
4. Rejected → SQS
5. Payment processing via Lambda
6. Analytics via QuickSight

##Technologies
- AWS S3
- AWS Lambda
- AWS Glue
- Amazon RDS
- Amazon SQS

# Features
- Automated validation
- Serverless architecture
- Scalable pipeline
