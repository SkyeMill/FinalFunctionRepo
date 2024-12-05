import kagglehub
import os
import pandas as pd
import boto3

def main():
    # Set parameters for object-oriented upload
    DO_SPACES_ACCESS_KEY = os.environ["spaces_access_key"]
    DO_SPACES_SECRET_KEY = os.environ["spaces_secret_key"]
    DO_SPACES_REGION = 'sfo3'  # or your specific region
    DO_SPACES_ENDPOINT = 'http://preprocessed-data.sfo3.digitaloceanspaces.com'

    # Initialize a session using your Spaces credentials
    session = boto3.session.Session()
    client = session.client('s3',
                            region_name=DO_SPACES_REGION,
                            endpoint_url=DO_SPACES_ENDPOINT,
                            aws_access_key_id=DO_SPACES_ACCESS_KEY,
                            aws_secret_access_key=DO_SPACES_SECRET_KEY)

    # Define the name of your Space and the file you want to upload
    space_name = 'preprocessed-data'

    # Download latest version
    path = kagglehub.dataset_download("rabieelkharoua/students-performance-dataset")
    print("Path to dataset files:", path)
    data_files_directory = os.listdir(path)

    for data_file in data_files_directory:
        file_name = os.path.join(path, data_file)
        print("FILE NAME: ", file_name)
        
        # Use the original file name as part of the object name to avoid overwriting
        object_name = f"Preprocessed_Data/{data_file}"
        print("OBJECT NAME", object_name)

        # Upload the file
        client.upload_file(file_name, space_name, object_name)
        print(f'{file_name} has been uploaded to {space_name} as {object_name}')

    return {
        'statusCode': 200,
        'body': 'Files uploaded successfully!'
    }
main()