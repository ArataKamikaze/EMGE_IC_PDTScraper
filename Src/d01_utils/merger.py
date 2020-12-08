import os
import glob
import pandas as pd
from pathlib import Path

def merger():
    path = Path('../../Data/01_raw')
    os.chdir(path)
    print(path)
    all_filenames = [i for i in glob.glob('*.{}'.format('csv'))]

    print(all_filenames)

    combined_csv = pd.concat([pd.read_csv(str(path)+ '\\'+ str(f), encoding='ANSI', sep="pandas", engine="python") for f in all_filenames])
    combined_csv.to_csv('../../Data/01_raw/combined.csv', encoding="ANSI", index=False)
