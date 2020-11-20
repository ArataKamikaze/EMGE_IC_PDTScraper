import requests
from zipfile import ZipFile
import os as os
from pathlib import Path
from .setup import setup
from . import Definitions as d

def downloadZip(mes_Min, ano_Min, mes_Max, ano_Max, link, nome):
    setup()
    url = d.definitions(link)[0]
    while 1 == 1:
        if not (mes_Min != mes_Max or ano_Min != ano_Max):
            break;
        if mes_Min <= 9:
            url = url + '/' + str(ano_Min) + '0' + str(mes_Min)
        else:
            url = url + '/' + str(ano_Min) + str(mes_Min)
        print(url)
        mes_Min += 1
        if mes_Min == 12:
            ano_Min = ano_Min + 1
            mes_Min = 1

downloadZip(1,2020,6,2020,'contratos', 'oi')

# def downloadZip(dia_Min, mes_Min, ano_Min, dia_Max, mes_Max, ano_Max, link, nome):
#     setup()
#     while (mes_Min != mes_Max or mes_Min != mes_Max || dia_Min != dia_Max):


# def getFiles(mes_Min, ano_Min, mes_Max, ano_Max, link, nome):
#     while 1 == 1:
#         if mes_Min <= 9:
#             url = link + '/' + str(ano_Min) + '0' + str(mes_Min)
#         else:
#             url = link + '/' + str(ano_Min) + str(mes_Min)
#         print(url)
#
#         request = requests.get(url, allow_redirects=True)
#         if mes_Min <= 9:
#             open('files/' + nome + '/' + nome + str(ano_Min) + '-' + '0' + str(mes_Min) + '.zip', 'wb').write(
#                 request.content)
#             unziper('files/' + nome + '/' + nome + str(ano_Min) + '-' + '0' + str(mes_Min) + '.zip')
#             add_to_dataframe()
#         else:
#             open('files/' + nome + '/' + nome + str(ano_Min) + '-' + str(mes_Min) + '.zip', 'wb').write(request.content)
#             unziper('files/' + nome + '/' + nome + str(ano_Min) + '-' + str(mes_Min) + '.zip')
#             add_to_dataframe()
#
#         print(request.headers.get('content-type'))
#         mes_Min = mes_Min + 1
#         if mes_Min == 12:
#             ano_Min = ano_Min + 1
#             mes_Min = 1
#         if ano_Min == ano_Max and mes_Min == mes_Max + 1:
#             break