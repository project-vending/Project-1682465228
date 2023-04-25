python
import boto3
import pandas as pd

# Connect to S3
s3 = boto3.client('s3')

# Specify the bucket and object/key name
bucket_name = 'your-bucket-name'
object_key = 'data/raw_data.csv'

# Read the file from S3 into a Pandas DataFrame
obj = s3.get_object(Bucket=bucket_name, Key=object_key)
df = pd.read_csv(obj['Body'])

# Save the DataFrame as a CSV file in the data folder
df.to_csv('../data/raw_data.csv', index=False)
