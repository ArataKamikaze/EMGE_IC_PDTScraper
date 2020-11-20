import os as os
from pathlib import Path

def setup():

    if not Path('../../Data').is_dir():
        os.mkdir('../../Data')
    if not Path('../../Data/00_Zip').is_dir():
        os.mkdir('../../Data/00_Zip')
    if not Path('../../Data/01_raw').is_dir():
        os.mkdir('../../Data/01_raw')
    if not Path('../../Data/02_Processed').is_dir():
        os.mkdir('../../Data/02_Processed')