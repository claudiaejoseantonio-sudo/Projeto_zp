
# Codigo para ler um arquivo Excel usando a biblioteca pandas

import pandas as pd

# DeFinindo o caminho do arquivo Excel

caminho = "C:\\Teste_git\\dados\\nao_processado\\tabela_vendas_ZePequeno.xlsx"

# Lendo o arquivo Excel e armazenando em um DataFrame

zp = pd.read_excel(caminho)

# caso minha planilha tenha mais de uma aba, devo especificar a aba a ser analisada
# zp = pd.read_excel(caminho, sheet_name="Planilha1")

print(zp)

print(zp.columns)  # exibe as colunas do Dataframe
print(zp.head())   # exibe as primeiras linhas do Dataframe
print(zp.info())   # exibe informações sobre o Dataframe, como tipos de dados e valores nulos
print(zp.describe()) # exibe estatísticas descritivas para colunas numéricas

print(zp.columns)   
print(zp.head()) 
print(zp.info()) 
print(zp.describe())