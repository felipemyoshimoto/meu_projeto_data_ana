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
print("Média dos números;", modulos_importados["estatisticas"].media([10, 20, 30]))