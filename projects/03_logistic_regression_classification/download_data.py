import pandas as pd
import requests
import os

def download_diabetes_data():
    # Using the Pima Indians Diabetes dataset
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    file_path = "diabetes.csv"
    
    if not os.path.exists(file_path):
        print("Downloading Diabetes dataset...")
        response = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print("Download complete.")
    else:
        print("Diabetes dataset already exists.")

if __name__ == "__main__":
    download_diabetes_data()
