import os as os
import Definitions as d


def add_to_dataframe(path, date, name):
    for x in range(1, len(d.definitions(name))):
        for filename in os.listdir(path, date, ):
            if filename.endswith(+".csv") and filename.beginswith(date+d.definitions(name)[x]):
                print(os.path.join(path, filename))
            else:
                continue
