import pandas as pd
import requests
import os

def download_housing_data():
    # Using the Boston Housing dataset or similar public house price dataset
    url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
    filename = "housing.csv"
    
    # Get the directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    
    if not os.path.exists(file_path):
        print(f"Downloading {filename}...")
        response = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print("Download complete.")
    else:
        print(f"{filename} already exists in {current_dir}.")

if __name__ == "__main__":
    download_housing_data()
