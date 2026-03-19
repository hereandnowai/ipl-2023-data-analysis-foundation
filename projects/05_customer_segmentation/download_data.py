import pandas as pd
import requests
import os

def download_mall_data():
    # Using Mall Customer Segmentation dataset
    url = "https://raw.githubusercontent.com/SteffiPeTaffy/machineLearningAZ/master/Machine%20Learning%20A-Z%20Template%20Folder/Part%204%20-%20Clustering/Section%2024%20-%20K-Means%20Clustering/Mall_Customers.csv"
    file_path = "mall_customers.csv"
    
    if not os.path.exists(file_path):
        print("Downloading Mall Customers dataset...")
        response = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print("Download complete.")
    else:
        print("Mall Customers dataset already exists.")

if __name__ == "__main__":
    download_mall_data()
