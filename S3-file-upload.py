import boto3
import os
import time
from datetime import datetime
from pathlib import Path

# AWS S3 Configuration
AWS_ACCESS_KEY = 'your_access_key'
AWS_SECRET_KEY = 'your_secret_key'
BUCKET_NAME = 'your_bucket_name'

# Local folder path
DESKTOP_FOLDER = str(Path.home() / 'Desktop/your_folder')

# Initialize S3 client
s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

def upload_files_to_s3(folder_path, bucket_name):
    try:
        # List all files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                # Create a unique S3 key
                s3_key = f'{datetime.now().strftime("%Y-%m-%d/%H")}/{filename}'
                print(f'Uploading {filename} to {bucket_name}/{s3_key}')
                
                # Upload the file
                s3_client.upload_file(file_path, bucket_name, s3_key)
                print(f'Successfully uploaded {filename}')
                
                # Delete the file after uploading
                os.remove(file_path)
                print(f'Deleted {filename} from local folder')
    except Exception as e:
        print(f'Error uploading files: {e}')

def main():
    while True:
        # Upload files
        upload_files_to_s3(DESKTOP_FOLDER, BUCKET_NAME)
        
        # Wait for one hour before the next upload
        time.sleep(3600)  # 3600 seconds = 1 hour

if __name__ == '__main__':
    main()
