#!/usr/bin/env python
# coding: utf-8

import os
import tabula
import requests
import pandas as pd
from io import BytesIO


def create_dataframe_tjsp_debitos(input_path):
    # Requests
    url = 'https://www.tjsp.jus.br/Download/Tabelas/TabelaDebitosJudiciais.pdf'
    r = requests.get(url, allow_redirects=True)

    # Save PDF file
    open(os.path.join(input_path, 'tabela_debitos_judiciais.pdf'), 'wb').write(r.content)

    # Read PDF
    #dfs = tabula.read_pdf(os.path.join('data', 'tab_tjsp.pdf'), pages='all')
    dfs = tabula.read_pdf(BytesIO(r.content), pages='all')

    # Loop
    df_concat = pd.DataFrame()
    for n in range(len(dfs)):
        df = dfs[n]
        df.rename(columns={'Unnamed: 0': 'mes'}, inplace=True, errors='ignore')
        df.set_index('mes', inplace=True)
        df.drop('Unnamed: 1', axis=1, inplace=True, errors='ignore')
        df_concat = pd.concat([df_concat, df], axis=1)

    # Flat Dataframe
    df = df_concat
    df = df.stack()
    df = pd.DataFrame(df)
    df = df.reset_index()

    # Rename Columns
    df.rename(columns={'level_1': 'ano', 0: 'taxa'}, inplace=True, errors='ignore')

    # Rename Values
    dict_mes = {
        'JAN': 1,
        'FEV': 2, 
        'MAR': 3,
        'ABR': 4,
        'MAI': 5,
        'JUN': 6,
        'JUL': 7,
        'AGO': 8,
        'SET': 9,
        'OUT': 10,
        'NOV': 11,
        'DEZ': 12,
    }

    # Ajusta Mês
    df = df.replace({'mes': dict_mes})
    df['mes'] = df['mes'].astype(int)

    # Ajusta Ano
    df['ano'] = df['ano'].str.replace(' ', '')
    df['ano'] = df['ano'].astype(int)

    # Ajusta Taxa
    df['taxa_string'] = df['taxa']
    df['taxa'] = df['taxa'].str.replace('-', '', regex=True)
    df['taxa'] = df['taxa'].str.replace('.', '', regex=True)
    df['taxa'] = df['taxa'].str.replace(',', '.', regex=True)
    df = df[df['taxa'] != '']
    df['taxa'] = df['taxa'].astype(float).copy()

    # Ajusta Datas
    df['year'] = df['ano']
    df['month'] = df['mes']
    df['day'] = 1

    df['data'] = pd.to_datetime(df[['year', 'month', 'day']])
    df['data_ref'] = df['data'].dt.strftime('%Y-%m')

    # Drop
    df.drop(['year', 'month', 'day'], axis=1, inplace=True, errors='ignore')

    # Sortear
    df.sort_values('data', inplace=True)
    df = df.reindex(columns=['data', 'data_ref', 'ano', 'mes', 'taxa_string', 'taxa'], copy=True)
    df.reset_index(drop=True, inplace=True)

    print(df.tail(3))
    return df

if __name__ == "__main__":
    print('main!')