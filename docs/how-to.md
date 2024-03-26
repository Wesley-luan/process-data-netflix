# github

- utilizar o .gitignore, listando as pastas que voce nao quer subir para publico 

# o que vamos precisar
pandas e pip -> python

# conceitos

- virtual enviroment (venv) -> python -m venv venv

- para entrar no venv -> venv/scripts/activate

## etapas do dado

data raw -> todo dado antes de qualquer processamento e organizacao -> modelo de fabrica 

data ready -> o pos processo de tratamento dos arquivos do RAW

# draw diagram
tldraw.com

### pacotes instalados

pip install pandas
pip install openpyxl
pip install xlsxwriter

### tratamento Regras

- prezar pela confiabilidade e rastreabilidade dos dados
- add uma coluna com o nome do pais 
- pegar a campanha do utm-link



#### ETL
- Extract -> dados extraidos de outro lugar (data Raw)
- Transform -> tratamento ou transformacoes
- Load -> carregamento dos dados refinados (data Ready) -> BD, CSV, FileServer



### Import

import pandas -> clicaveis
import os -> manipular coisas no sistema
import glob -> englobamento de caminhos 