import pandas as pd
import requests
import os
import zipfile

def download_imdb_data():
    # Using a small subset of IMDB reviews
    url = "https://raw.githubusercontent.com/Aniruddha-Tapas/Base_Model_Sentiment_Analysis/master/IMDB_Dataset.csv"
    file_path = "imdb_reviews.csv"
    
    if not os.path.exists(file_path):
        print("Downloading IMDB dataset...")
        response = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print("Download complete.")
    else:
        print("IMDB dataset already exists.")

if __name__ == "__main__":
    download_imdb_data()
