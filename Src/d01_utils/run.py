from setup import setup as stp
from Downloader import Downloader as downL

stp.setup()
# downL.downloadZip(1,2020,2,2020,'contratos')
downL.downloadZip(1,2014,10,2020,'Execucao_despesa')

