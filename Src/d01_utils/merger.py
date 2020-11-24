import os
import glob
import pandas as pd
from pathlib import Path

path = Path('../../Data/01_raw')
os.chdir(path)

all_filenames = [i for i in glob.glob('*.{}'.format('csv'))]

print(all_filenames)

combined_csv = pd.concat([pd.read_csv(f, encoding='ansi', header=None, error_bad_lines=False, sep='delimiter') for f in all_filenames])
combined_csv.to_csv('../../Data/01_raw', index=False)
