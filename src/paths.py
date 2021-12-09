import os
import sys
from datetime import datetime

sys.path.append(os.getcwd())
import src.update_tjsp_taxas as tjsp

#print('Pasta raiz é: "{}" e tem o seguinte conteudo:\n'.format(os.getcwd()))
#print(os.listdir(os.getcwd()))

#print('Pasta anterior é: "{}" e tem o seguinte conteudo:\n'.format(os.path.join(os.getcwd(), '..')))
#print(os.listdir(os.path.join(os.getcwd(), '..')))

# Create Directory and Save file
input_path = os.path.join('data')
os.makedirs(input_path, exist_ok=True)

# Only to change
date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
with open(os.path.join(input_path, 'readme.txt'), 'w') as f:
    f.write('date and time: {}'.format(date_time))

# Create Dataframe
df = tjsp.create_dataframe_tjsp_debitos(input_path)

# Save "tabela_debitos_judiciais"
df.to_csv(
    os.path.join(input_path, 'tabela_debitos_judiciais.csv'),
    index=False,
    decimal=',',
)
