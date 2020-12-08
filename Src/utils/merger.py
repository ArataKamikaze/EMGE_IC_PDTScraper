import os
import glob
import pandas as pd
from pathlib import Path

path = r'D:\\EMGE\\2020\\IC\\dev\\EMGE_IC_PDTScraper\\Data\\01_raw\\'
all_filenames = glob.glob(path + '*.{}'.format('csv'))

dfDtypes = None
all_data_frames = []

for f in all_filenames:
    df = pd.read_csv(f, index_col=None, header=0, dtype=dfDtypes,
                     encoding='ANSI', sep=';', low_memory=False)
    if dfDtypes == None:
        dfDtypes = df.dtypes.to_dict()

    all_data_frames.append(df)

combined_csv = pd.concat(all_data_frames)

combined_csv.to_csv('Data/02_Processed/2020_Despesas.csv', index=False)

combined_csv.info()
