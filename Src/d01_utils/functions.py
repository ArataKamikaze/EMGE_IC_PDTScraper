import os as os
from Definitions import definitions

def add_to_dataframe(path, date, name):
    for x in range(1, definitions(name)):
        for filename in os.listdir(path, date, ):
            if filename.endswith(+".csv") and filename.beginswith(date+definitions[x]):
                print(os.path.join(path, filename))
            else:
                continue