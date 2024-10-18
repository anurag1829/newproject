import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def copy_s3_data(source_bucket, source_key, destination_bucket, destination_key):
    s3 = boto3.client('s3')
    try:
        copy_source = {
            'Bucket': source_bucket,
            'Key': source_key
        }
        s3.copy(copy_source, destination_bucket, destination_key)
        print(f"File copied from {source_bucket}/{source_key} to {destination_bucket}/{destination_key}")
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    source_bucket = 'customer-source-bucket'
    source_key = 'path/to/source/file'
    destination_bucket = 'my-destination-bucket'
    destination_key = 'path/to/destination/file'
    
    copy_s3_data(source_bucket, source_key, destination_bucket, destination_key)
