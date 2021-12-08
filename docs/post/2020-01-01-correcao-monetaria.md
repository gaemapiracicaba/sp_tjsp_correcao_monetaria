---
title: "Correção Monetária"
date: 2021-11-01T12:00:00-03:00
last_modified_at: 2021-11-01T12:00:00-03:00
excerpt_separator: "<!--more-->"
toc: false
categories:
  - blog
tags:
  - recursos hídricos
  - qualidade
  - enquadramento
  - água bruta
classes: wide
author: Michel Metran
comments: false
excerpt: Sistema para acesso aos dados de qualidade de água superficial (dos rios)
share: false
related: false
header:
  overlay_image: /assets/correcao_monetaria/imgs/river-min.jpg
  overlay_filter: 0.5 # same as adding an opacity of 0.5 to a black background
  caption: "Foto: [**Fabricio Macedo**](https://pixabay.com/pt/users/fabriciomacedophotos-328534/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1729544)"
  actions:
    - label: "Mais informações"
      url: "https://sistemainfoaguas.cetesb.sp.gov.br/"
---

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

Descrever...

<br>

É possível também acessar a tabela em formatos *.csv* e *.pdf* nos botões abaixo:

<a href="https://gaemapiracicaba.github.io/assets/correcao_monetaria/data/tabela_debitos_judiciais.csv" class="btn btn--primary">Download *csv*</a>

<a href="https://gaemapiracicaba.github.io/assets/correcao_monetaria/data/tabela_debitos_judiciais.pdf" class="btn btn--primary">Download *pdf*</a>
