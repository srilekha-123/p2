from google.cloud import storage
from google.oauth2 import service_account

def upload_files_GCS(bucket_name, source_file_name, destination_blob_name):
    try:
        # Specify the path to your service account key file
        credentials = service_account.Credentials.from_service_account_file(
            'C:\\Users\\yeruv\\Downloads\\crack-solstice-432414-k6-c380ea9f8c10.json'
        )
        
        # Create a storage client with the credentials
        storage_client = storage.Client(credentials=credentials, project='batch5')

        # Get the bucket
        bucket = storage_client.bucket(bucket_name)
        
        # Create a new blob and upload the file's content
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
    
        print(f"File {source_file_name} uploaded to {destination_blob_name}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
bucket_name1 = "revprop25"
source_file_name1 = "cleaned.csv"
destination_blob_name1 = "cleaned.csv"
upload_files_GCS(bucket_name1, source_file_name1, destination_blob_name1)
bucket_name2 = "revprop25"
source_file_name2 = "rogue.csv"
destination_blob_name2 = "rogue.csv"
upload_files_GCS(bucket_name2, source_file_name2, destination_blob_name2)