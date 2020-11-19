import bib as Bib
import pandas as pd
"""
O método a seguir realiza o download dos arquivos zip contendo os arquivos csv do site do portal da transparência.

Os parâmetros em ordem significam:
mes_Inicial: O mês inicial da busca
ano_Inicial: O ano inicial da busca
mes_Final: O mês final da busca
ano_Final: O mês final da busca
link: link da página do que deseja baixar
nome: nome que será dado aos arquivos e à pasta onde eles serão salvos dentro da pasta files na raíz do projeto
"""
ds = pd.DataFrame()
Bib.run(9,2020,10,2020,'http://www.portaltransparencia.gov.br/download-de-dados/compras','teste', ds)
