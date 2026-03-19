import pandas as pd
import requests
import os

def download_apple_stock():
    # Public Apple stock history from Yahoo Finance via static CSV link
    url = "https://raw.githubusercontent.com/mwitiderrick/stockwise/master/AAPL.csv"
    file_path = "apple_stock.csv"
    
    if not os.path.exists(file_path):
        print("Downloading Apple Stock dataset...")
        response = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print("Download complete.")
    else:
        print("Apple stock dataset already exists.")

if __name__ == "__main__":
    download_apple_stock()
