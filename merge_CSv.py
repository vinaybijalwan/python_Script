# Merge Multiple 1M Rows CSV files
import os

import pandas as pd

# 1. defines path to csv files
path = "C:/Users/vinay_bijalwan.PATANJALI/Desktop/data"

#cwd = os.getcwd()

# 2. creates list with files to merge based on name convention
file_list = [path + f for f in os.listdir(path) if f.startswith('ChikitshalyaReport_')]

# 3. creates empty list to include the content of each file converted to pandas DF
csv_list = []

# 4. reads each (sorted) file in file_list, converts it to pandas DF and appends it to the csv_list
for file in sorted(file_list):
    csv_list.append(pd.read_csv(file).assign(File_Name = os.path.basename(file)))


# 5. merges single pandas DFs into a single DF, index is refreshed 
csv_merged = pd.concat(csv_list, ignore_index=True)

# 6. Single DF is saved to the path in CSV format, without index column
csv_merged.to_csv(path + 'patient_data.csv', index=False)
