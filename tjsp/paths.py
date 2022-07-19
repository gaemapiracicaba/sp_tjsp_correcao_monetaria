#!/usr/bin/env python
# coding: utf-8

import pprint
from pathlib import Path

project_path = Path(__file__).absolute().parents[1]
package_path = project_path / 'tjsp'
data_path = package_path / 'data'
data_path.mkdir(exist_ok=True)

if __name__ == '__main__':
    print(f'Pasta raiz é: "{project_path}" e tem o seguinte conteudo:')
    pprint.pprint(list(project_path.glob('*.*')))
