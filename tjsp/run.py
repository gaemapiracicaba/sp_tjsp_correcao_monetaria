#!/usr/bin/env python
# coding: utf-8

from paths import *
from datetime import datetime
import update_tjsp_taxas as tjsp


# Only to change
date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
with open(data_path / 'date.txt', 'w') as f:
    f.write(f'Data: {date_time}')


# Create Dataframe
df = tjsp.create_dataframe_tjsp_debitos(data_path)


# Save "tabela_debitos_judiciais"
df.to_csv(
    data_path / 'tabela_debitos_judiciais.csv',
    index=False,
    decimal=',',
)
