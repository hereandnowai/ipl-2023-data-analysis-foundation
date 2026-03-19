import pandas as pd
import requests
import os

def download_supermarket_data():
    # Using supermarket sales dataset
    url = "https://raw.githubusercontent.com/manneyliu/supermarket-sales-data-analysis/master/supermarket_sales.csv"
    file_path = "supermarket_sales.csv"
    
    if not os.path.exists(file_path):
        print("Downloading Supermarket Sales dataset...")
        response = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print("Download complete.")
    else:
        print("Supermarket Sales dataset already exists.")

if __name__ == "__main__":
    download_supermarket_data()
