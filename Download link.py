import requests
from bs4 import BeautifulSoup
import json
import os

# File to store already recorded files
RECORDED_FILES = "recorded_files.json"

# Initialize or load recorded files
if os.path.exists(RECORDED_FILES):
    with open(RECORDED_FILES, "r") as file:
        recorded_files = json.load(file)
else:
    recorded_files = {}

def fetch_files(url):
    try:
        # Fetch the webpage content
        response = requests.get(url, verify=False)  # `verify=False` is used for self-signed SSL certificates
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Parse the links and details
        files = []
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and "AFS" in href:  # Filter for files containing "AFS"
                file_name = href.split("/")[-1]
                parent = link.find_next_sibling(text=True)
                if parent:
                    details = parent.strip().split()
                    if len(details) >= 2:
                        date, time = details[:2]
                        files.append({
                            "file_name": file_name,
                            "download_link": url + file_name,
                            "date": date,
                            "time": time,
                        })
        return files
    except Exception as e:
        print(f"Error fetching files: {e}")
        return []

def save_new_files(files):
    new_files = [f for f in files if f["file_name"] not in recorded_files]
    if new_files:
        for file in new_files:
            recorded_files[file["file_name"]] = file
        with open(RECORDED_FILES, "w") as file:
            json.dump(recorded_files, file, indent=4)
        print(f"Added {len(new_files)} new file(s):")
        for file in new_files:
            print(f"  - {file['file_name']}")
    else:
        print("No new files found.")

if __name__ == "__main__":
    URL = "https://114.130.69.204/RECORDINGS/MP3/"  # Replace with your actual URL
    print("Fetching files...")
    all_files = fetch_files(URL)
    save_new_files(all_files)
