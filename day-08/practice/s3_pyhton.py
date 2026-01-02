import boto3

s3 = boto3.client("s3")
response = s3.list_buckets()
print("Existing S3 buckets are: ")
for key in response["Buckets"]:
    print(key["Name"])