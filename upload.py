from google.cloud import storage

# Function to upload a file to GCS
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name} in {bucket_name}.")

# Upload raw and cleaned data to GCS
bucket_name = 'bucket05'
upload_to_gcs(bucket_name, 'rogue.csv', 'rogue.csv')
upload_to_gcs(bucket_name, 'cleaned.csv', 'cleaned.csv')