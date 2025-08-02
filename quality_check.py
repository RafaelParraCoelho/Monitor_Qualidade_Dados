import pandas as pd

# Função para carregar os dados a partir de um arquivo CSV
def carregar_dados(caminho):
    return pd.read_csv(caminho)

# Função para verificar quantos valores nulos existem em cada coluna
def verificar_nulos(df):
    return df.isnull().sum()

# Função para contar quantas linhas duplicadas existem no DataFrame
def verificar_duplicatas(df):
    return df.duplicated().sum()

# Função para mostrar os tipos de dados de cada coluna
def verificar_tipos(df):
    return df.dtypes

# Função principal que gera o relatório de qualidade dos dados
def gerar_relatorio(df):
    print(" Colunas com valores nulos:")
    print(verificar_nulos(df))
    
    print("\n Número de linhas duplicadas:")
    print(verificar_duplicatas(df))
    
    print("\n Tipos de dados por coluna:")
    print(verificar_tipos(df))

# Se o arquivo for executado diretamente, ele roda essa parte
if __name__ == "__main__":
    # Caminho para o arquivo CSV (ajuste conforme sua pasta)
    df = carregar_dados("data/exemplo.csv")
    
    # Gerar o relatório de qualidade de dados
    gerar_relatorio(df)
