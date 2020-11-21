from setup import setup as stp
from Downloader import Downloader as downL

stp.setup()
# downL.downloadZip(1,2020,2,2020,'contratos')
downL.downloadZipday(1,1,2020,10,1,2020,'empenho_liquidacao_pagamento')

