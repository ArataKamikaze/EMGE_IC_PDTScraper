import requests
from zipfile import ZipFile
import setup
import Definitions
import os as os


def unzipper(file):
    with ZipFile(file, 'r') as zipObj:
        zipObj.extractall('Data/01_raw')
    os.remove(file)


def downloadZip(mes_Min, ano_Min, mes_Max, ano_Max, nome):
    setup.setup()
    end = 1
    while 1 == 1:
        url = Definitions.definitions(nome)[0]
        if mes_Min <= 9:
            url = url + '/' + str(ano_Min) + '0' + str(mes_Min)
        else:
            url = url + '/' + str(ano_Min) + str(mes_Min)
        print(url)

        request = requests.get(url, allow_redirects=True)
        print(request.headers.get('content-type'))
        if mes_Min <= 9:
            open('Data/00_Zip/' + nome + str(ano_Min) + '-' +
                 '0' + str(mes_Min) + '.zip', 'wb').write(request.content)
            unzipper('Data/00_Zip/' + nome + str(ano_Min) +
                     '-' + '0' + str(mes_Min) + '.zip')
        else:
            open('Data/00_Zip/' + nome + str(ano_Min) + '-' +
                 str(mes_Min) + '.zip', 'wb').write(request.content)
            unzipper('Data/00_Zip/' + nome +
                     str(ano_Min) + '-' + str(mes_Min) + '.zip')
        mes_Min += 1
        if mes_Min == 12:
            ano_Min = ano_Min + 1
            mes_Min = 1
        if end == 0:
            break
        if not (mes_Min != mes_Max or ano_Min != ano_Max):
            end = 0


def downloadZipday(dia_Min, mes_Min, ano_Min, dia_Max, mes_Max, ano_Max, nome):
    setup.setup()
    end = 1
    while 1 == 1:
        url = d.definitions(nome)[0]
        if mes_Min <= 9:
            url = url + '/' + str(ano_Min) + '0' + str(mes_Min)
            if dia_Min <= 9:
                url = url + '0' + str(dia_Min)
            else:
                url = url + str(dia_Min)
        else:
            url = url + '/' + str(ano_Min) + str(mes_Min)
            if dia_Min <= 9:
                url = url + '0' + str(dia_Min)
            else:
                url = url + str(dia_Min)
        print(url)

        request = requests.get(url, allow_redirects=True)
        print(request.headers.get('content-type'))
        if mes_Min <= 9:
            if dia_Min <= 9:
                open('Data/00_Zip/' + nome + str(ano_Min) + '-' + '0' + str(mes_Min) +
                     '-' + '0' + str(dia_Min) + '.zip', 'wb').write(request.content)
                unzipper('Data/00_Zip/' + nome + str(ano_Min) + '-' +
                         '0' + str(mes_Min) + '-' + '0' + str(dia_Min) + '.zip')
            else:
                open('Data/00_Zip/' + nome + str(ano_Min) + '-' + '0' + str(mes_Min) + '-' + str(dia_Min)+'.zip', 'wb').write(
                    request.content)
                unzipper('Data/00_Zip/' + nome + str(ano_Min) +
                         '-' + '0' + str(mes_Min) + '-' + str(dia_Min)+'.zip')

        else:
            if dia_Min <= 9:
                open('Data/00_Zip/' + nome + str(ano_Min) + '-' + str(mes_Min) + '-' + '0' + str(
                    dia_Min) + '.zip', 'wb').write(request.content)
                unzipper('Data/00_Zip/' + nome + str(ano_Min) + '-' + str(mes_Min) + '-' + '0' + str(
                    dia_Min) + '.zip')
            else:
                open('Data/00_Zip/' + nome + str(ano_Min) + '-' + str(mes_Min) + '-' + str(
                    dia_Min) + '.zip', 'wb').write(
                    request.content)
                unzipper('Data/00_Zip/' + nome + str(ano_Min) + '-' + str(mes_Min) + '-' + str(
                    dia_Min) + '.zip')
        dia_Min += 1
        if (ano_Min % 400 == 0 or ano_Min % 4 == 0 and ano_Min % 100 == 0) and mes_Min == 2:
            if dia_Min == 29:
                mes_Min += 1
                dia_Min = 1
        elif mes_Min == 2:
            if dia_Min == 28:
                mes_Min += 1
                dia_Min = 1
        if (mes_Min == 1 or mes_Min == 3 or mes_Min == 5 or mes_Min == 7 or mes_Min == 8 or mes_Min == 10 or mes_Min == 12) and dia_Min == 31:
            mes_Min += 1
            dia_Min = 1
        if (mes_Min == 4 or mes_Min == 6 or mes_Min == 9 or mes_Min == 11) and dia_Min == 30:
            mes_Min += 1
            dia_Min = 1
        if mes_Min == 13:
            ano_Min = ano_Min + 1
            mes_Min = 1
        if end == 0:
            break
        if not (mes_Min != mes_Max or ano_Min != ano_Max or dia_Min != dia_Max):
            end = 0
