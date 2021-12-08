# Correção Monetária de Débitos Judiciais

<br>

O [Tribunal de Justiça do Estado de São Paulo](https://www.tjsp.jus.br/) disponibiliza mensalmente as taxas para calcular a correção monetária de multas e débitos judiciais. As taxas atualizadas são divulgadas por meio de um arquivo em formato *.pdf*.
- [TabelaDebitosJudiciais.pdf](https://www.tjsp.jus.br/Download/Tabelas/TabelaDebitosJudiciais.pdf)

<br>

O repositório [gaemapiracicaba/correcao_monetaria](https://github.com/gaemapiracicaba/correcao_monetaria) visa criar uma função para converter esse arquivo _.pdf_ em formato tabular (_.csv_) e disponibilizar isso de maneira facilitada, por meio de um servidor, com atualização periódica!

<br>

---

## Como Usar?

O arquivo _.csv_ disponível no servidor é atualizado todas as terças-feiras, as 7h00 e fica disponível no endereço a seguir:

- https://gaemapiracicaba.github.io/assets/correcao_monetaria/data/tabela_debitos_judiciais.csv

<br>

### *Google Spreadsheets*

Uma vez que o arquivo _.csv_ está disponível em um servidor, é possível utilizar a função **_=IMPORTDATA()_** do _Google Spreadsheets_ para acessa-lo diretamente na tabela, possibilitando cálculos etc.

![](https://i.imgur.com/oFdGGbA.png)

<br>

Visando auxiliar essa etapa, [_já foi criada uma tabela com a função_](https://docs.google.com/spreadsheets/d/1xOH1QN8qsZ3-_u6p1dbhIZ2N4IvSBbMJucM1BhXf8Sw/edit?usp=sharing), bastando criar uma cópia da tabela para sua conta _Google_.

<br>

### *Microsoft Excel*

