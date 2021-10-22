import pandas as pd
from pprint import pprint
import json
import os
import glob

# use glob to get all the csv files
# in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))


for f in csv_files:
    # read the csv file
    df = pd.read_csv(f, sep=';', encoding='PT154', comment='#')

    print('Location:', f)
    print('File Name:', f.split("\\")[-1])

  
    print('Content:')
    print(df.head(10))
    print()
    
    


df13=pd.read_excel('dataset_knigi_1.xlsx', index_col=None, header=None)
print(df13.head())

with open('books.jsn', 'r', encoding='utf-8') as f:  # открыли файл с данными
    text = json.load(f)  # загнали все, что получилось в переменную
    pprint(text)
    
