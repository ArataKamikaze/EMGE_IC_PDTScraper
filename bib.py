import requests
from zipfile import ZipFile
import os as arquivos
from pathlib import Path
import numpy as np



def run(mes_Min, ano_Min, mes_Max, ano_Max, link, nome):
    create_dataSet(nome)
    getFiles(mes_Min, ano_Min, mes_Max, ano_Max, link, nome)

def create_dataSet(nome):
    print("oi")
def getFiles(mes_Min, ano_Min, mes_Max, ano_Max, link, nome):


    if not Path('files').is_dir():
        arquivos.mkdir('files')

    if not Path('files/'+nome).is_dir():
        arquivos.mkdir('files/'+nome)


    while 1 == 1:
        if mes_Min <= 9:
            url = link +'/'+ str(ano_Min) + '0' + str(mes_Min)
        else:
            url = link + '/' +str(ano_Min) + str(mes_Min)


        print(url)


        request = requests.get(url, allow_redirects=True)
        if mes_Min <=9:
            open('files/'+ nome+'/'+nome + str(ano_Min) +'-' + '0' + str(mes_Min) + '.zip', 'wb').write(request.content)
            unziper('files/'+ nome+'/'+nome + str(ano_Min) +'-' + '0' + str(mes_Min) + '.zip')
        else:
            open('files/'+ nome+'/'+nome + str(ano_Min) +'-' + str(mes_Min) + '.zip', 'wb').write(request.content)
            unziper('files/'+ nome+'/'+nome + str(ano_Min) +'-' + str(mes_Min) + '.zip')
        print(request.headers.get('content-type'))
        mes_Min = mes_Min + 1
        if mes_Min == 12:
            ano_Min = ano_Min + 1
            mes_Min = 1
        if ano_Min == ano_Max and mes_Min == mes_Max+1:
            break

def unziper(file_Directory):
    with ZipFile(file_Directory, 'r') as zipObj:
                 zipObj.extractall('CSV')
