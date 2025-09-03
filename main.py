##from modulos import calculos as calc, estatisticas as est

##resultado = calc.soma(5, 7)
##print("Resultado:", resultado)

##med_total = est.media([10, 20, 30])
##print("Média:", med_total)

import importlib
import os

#Importando todos os módulos dinamnicamente

arquivos_modulos = [f.replace(".py", "") for f in os.listdir("modulos") if f.endswith(".py") and f != "__init__.py"]
modulos_importados = {}
for nome in arquivos_modulos:
    modulos_importados[nome] = importlib.import_module(f"modulos.{nome}")

#Exemplo de uso dos módulos
print("Soma 5 + 7", modulos_importados["calculos"].soma(5, 7))

#Nova Parte: Aula 4 - Análise de Dados com Pandas
from modulos import analise

#Carregando um arquivo CSV
df = analise.carregar_csv("dados.csv")

#Mostar primeiras linhas
print(" Dados do arquivo CSV:")
print(df)

#Estatísticas
print("\n Estatísticas básicas:")
print(analise.estatistica_basica(df))

#Selecionar uam coluna
print("\n Idades:")
print(analise.selecionar_coluna(df, "idade"))

