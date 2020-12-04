
def definitions(set):
    licitacoes = ['http://www.portaltransparencia.gov.br/download-de-dados/licitacoes/',
                  'ItemLicitação',
                  'Licitação',
                  'ParticipantesLicitação']

    contratos = ['http://www.portaltransparencia.gov.br/download-de-dados/compras',
                 'Compras',
                 'ItemCompra',
                 'TermoAditivo',
                 'Apostilamento']

    empenho_liquidacao_pagamento = ['http://www.portaltransparencia.gov.br/download-de-dados/despesas',
                'Despesas_Empenho',
                'Despesas_ItemEmpenho',
                'Despesas_Liquidacao',
                'Despesas_Liquidacao_EmpenhosImpactados',
                'Despesas_Pagamento',
                'Despesas_Pagamento_EmpenhosImpactados',
                'Despesas_Pagamento_FavorecidosFinais',
                'Despesas_Pagamento_ListaBancos',
                'Despesas_Pagamento_ListaFaturas',
                'Despesas_Pagamento_ListaPrecatorios',]

    Execucao_despesa = ['http://www.portaltransparencia.gov.br/download-de-dados/despesas-execucao',
                        'Despesas']

    Recursos_transferidos = ['http://www.portaltransparencia.gov.br/download-de-dados/transferencias',
                             'Transferencias']

    Recursos_por_favorecido = ['http://www.portaltransparencia.gov.br/download-de-dados/despesas-favorecidos',
                               'RecebimentosRecursosPorFavorecido']

    Execucao_da_Receita = ['http://www.portaltransparencia.gov.br/download-de-dados/receitas',
                           'Receitas']

    if set == "licitacoes":
        return licitacoes
    elif set == "contratos":
        return contratos
    elif set == "empenho_liquidacao_pagamento":
        return empenho_liquidacao_pagamento
    elif set == "Execucao_despesa":
        return Execucao_despesa
    elif set == "Recursos_transferidos":
        return Recursos_transferidos
    elif set == "Recursos_por_favorecido":
        return Recursos_por_favorecido
    elif set == "Execucao_da_Receita":
        return Execucao_da_Receita