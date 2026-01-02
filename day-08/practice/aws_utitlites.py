import boto3
import pdb


class AWSUtils:
    def __init__(self):
        self.s3 = self.get_connection("s3")
        self.ec2= self.get_connection("ec2")

    def get_connection(self,service):
        return boto3.client(service)

    def show_bucket(self):
        response = self.s3.list_buckets()
        print("Existing S3 buckets are: ")
        for key in response["Buckets"]:
            print(key["Name"])

    def create_bucket(self, bucket_name):
        try:
            respone= self.s3.create_bucket(
                Bucket=bucket_name,
                )
            if respone['ResponseMetadata']["HTTPStatusCode"]==200:
                print("bucket is created sucessfully")
    
        except:
            print("Error Occure")
    def upload_file_to_s3(self, file_path, bucket_name,key_name):
        self.s3.upload_file(file_path, bucket_name, key_name)
        print("File Uploaded Successfully")

    
    def put_object_s3(self,file_content, bucket_name, objectkey):
        self.s3.put_object( 
            Body=file_content,
            Bucket=bucket_name,
            Key=objectkey,
        )
        print("has been put successfully ")
    
    def show_region(self):
        response = self.ec2.describe_regions()
        print(response)


 

#show_bucket(client_s3)
#create_bucket(client_s3, "rahman-ki-bucket-0101243")
#upload_file_to_s3(client_s3, "output1.json",  "rahman-ki-bucket-0101243", "output.json")
#put_object_s3(client_s3,"Thisis new contenet","rahman-ki-bucket-0101243","output1.json" )

if __name__ == "__main__":
    aws = AWSUtils()
    aws.show_bucket()
    aws.create_bucket("rahman-ki-bucket-0101243")
    aws.upload_file_to_s3("output1.json", "rahman-ki-bucket-0101243", "output.json" )