import requests
import os
import numpy as np

def download_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    filename = "titanic.csv"
    
    # Get the directory where the script is located
    # This ensures the data stays in the project folder even if run from the root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    
    if not os.path.exists(file_path):
        print(f"Downloading {filename} to {current_dir}...")
        response = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print("Download complete.")
    else:
        print(f"{filename} already exists in {current_dir}.")

download_data()