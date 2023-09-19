## import lib

import pandas as pd
import os
import glob

#list all csv files only
csv_files = glob.glob('*.{}'.format('csv'))
csv_files
##concate csv file in loop
df_concat = pd.concat([pd.read_csv(f, encoding='ISO 8859-1') for f in csv_files ], ignore_index=True)

##save file as csv
df_concat.to_csv('2016_2022.csv')