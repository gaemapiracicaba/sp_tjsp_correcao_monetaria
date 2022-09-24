"""


"""



import sys
import tabula
import requests
import pandas as pd
from io import BytesIO


from pathlib import Path


def get_data():
    # Requests
    url = 'https://www.tjsp.jus.br/Download/Tabelas/TabelaDebitosJudiciais.pdf'
    r = requests.get(url, allow_redirects=True)
    return r


def save_pdf(input_path):
    # Requests
    r = get_data()

    # Save PDF file
    open(input_path / 'tabela_debitos_judiciais.pdf', 'wb').write(r.content)

    return 0


def get_table():
    # Requests
    r = get_data()

    # Read PDF
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
    return df

