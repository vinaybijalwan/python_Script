import os
import csv
from datetime import datetime

folder_path = 'C:/Users/vinay_bijalwan.PATANJALI/Desktop/website_project'     
csv_file = 'folders.csv'

# Get list of all folders in the given folder path
folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

# Get last modified date for each folder
folder_data = [[f, datetime.fromtimestamp(os.path.getmtime(os.path.join(folder_path, f))).strftime('%Y-%m-%d %H:%M:%S')] for f in folders]

# Write data to CSV file
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Folder Name', 'Last Modified Date'])
    writer.writerows(folder_data)

print(f'Successfully written folder information to {csv_file}')
