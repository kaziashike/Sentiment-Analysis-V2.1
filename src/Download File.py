import os
import requests
from datetime import datetime
import json
from Processing import Processing
from extract import extractData

# Function to download files within the specified range
def download_files(json_file, start_datetime, end_datetime, download_folder):
    # Load JSON data from the file
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    # Ensure the download folder exists
    os.makedirs(download_folder, exist_ok=True)

    # Iterate through the JSON data
    for item in json_data.values():
        file_datetime_str = f"{item['date']} {item['time']}"
        file_datetime = datetime.strptime(file_datetime_str, "%Y-%m-%d %H:%M")

        # Check if the file falls within the date and time range
        if start_datetime <= file_datetime <= end_datetime:
            file_name = item['file_name']
            file_path = os.path.join(download_folder, file_name)

            # Skip if the file already exists
            if os.path.exists(file_path):
                print(f"File already exists: {file_name}")
                continue

            # Download the file
            download_link = item['download_link']
            try:
                response = requests.get(download_link, stream=True, verify=False)
                response.raise_for_status()
                with open(file_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                print(f"Downloaded: {file_name}")
                

            except requests.exceptions.RequestException as e:
                print(f"Failed to download {file_name}: {e}")
            ############################################################
            procecessing_result = Processing(file_path)
            print(procecessing_result)
            

            
            ############################################################

# User-provided date and time range
start_datetime = datetime.strptime("2025-1-24 22:00", "%Y-%m-%d %H:%M")
end_datetime = datetime.strptime("2025-1-25 4:21", "%Y-%m-%d %H:%M")

# JSON file containing the data
json_file = "recorded_files.json"

# Folder to save downloaded files
download_folder = "download"

# Run the download function
download_files(json_file, start_datetime, end_datetime, download_folder)
