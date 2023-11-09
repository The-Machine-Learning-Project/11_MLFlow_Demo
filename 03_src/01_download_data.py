# Download data from UCI Machine Learning Repository

# Import libraries
import pandas as pd
import zipfile
import urllib.request

# URL to the zip file
zip_url = "https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip"

# Download the zip file
zip_file_path = "default+of+credit+card+clients.zip"
urllib.request.urlretrieve(zip_url, zip_file_path)

# Extract the CSV file from the downloaded zip
with zipfile.ZipFile(zip_file_path, 'r') as zip_file:

    zip_file_list = zip_file.namelist()
    print(zip_file_list)
    
    # Find the first file with a .xls extension
    xls_file_name = next((file for file in zip_file_list if file.endswith('.xls')), None)
    
    if xls_file_name:
        with zip_file.open(xls_file_name) as xls_file:
            data = pd.read_excel(xls_file)
            data.to_csv(r'01_data/01_raw/credit_card_data.csv')  # Save the CSV data to a local file
    else:
        print("No XLS file found in the zip archive.")

# Remove the downloaded zip file
import os
os.remove(zip_file_path)
