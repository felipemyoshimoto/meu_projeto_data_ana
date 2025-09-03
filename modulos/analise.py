import pandas as pd

def carregar_csv(caminho):
    """
    Lê um arquivo csv e retorna um Dataframe do pandas.
    """
    return pd.read_csv(caminho)

def estatistica_basica(df):
    """
    Retorna estatísticas descritivas do DataFrame.
    """
    return df.describe()

def selecionar_coluna(df, coluna):
    """
    Retorna uma coluna específica do dataFrame.
    """
    return df[coluna]
    
