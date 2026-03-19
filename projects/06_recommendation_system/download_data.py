import pandas as pd
import requests
import os
import zipfile

def download_movielens():
    # MovieLens 100k summary
    url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
    zip_path = "movielens.zip"
    
    if not os.path.exists("movies.csv"):
        print("Downloading MovieLens dataset...")
        response = requests.get(url)
        with open(zip_path, "wb") as f:
            f.write(response.content)
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(".")
            
        print("Extracting files...")
        os.rename("ml-latest-small/movies.csv", "movies.csv")
        os.rename("ml-latest-small/ratings.csv", "ratings.csv")
