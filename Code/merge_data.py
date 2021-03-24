# Merging output files as one integrated file

# Importing required packages
import pandas as pd
import numpy as np
import glob
import sys
import datetime
import shutil
import os

# Defining file path for integrated file
excel_file_path = '/Users/han.jw/Documents/Jae W. Han/Python/Project/Airfare Tracker/merged data/'
now = datetime.datetime.now()
date = now.strftime('%Y%m%d')

# Union files
all_data = pd.DataFrame()
for f in glob.glob('/Users/han.jw/Documents/Jae W. Han/Python/Project/Airfare Tracker/output/*.xlsx') :
 df = pd.read_excel(f)
 all_data = all_data.append(df, ignore_index=True)

# Check the data
print(all_data.shape)
all_data.head()

# Save the data as one file
all_data.to_excel(excel_file_path+'price_'+date+'.xlsx', header=True, index=False)

# Delete output files
files = glob.glob('/Users/han.jw/Documents/Jae W. Han/Python/Project/Airfare Tracker/output/*.xlsx')
for f in files :
 os.remove(f)