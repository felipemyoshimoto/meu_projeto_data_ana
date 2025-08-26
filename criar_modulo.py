import os 

nome_modulo = input("Digite o nome do novo módulo: ") # ex: funcoes
caminho = f"modulos/{nome_modulo}.py"

if not os.path.exists(caminho):
    with open(caminho, "w") as arquivo:
        arquivo.write("# Novo módulo\n")
    print(f"Módulo '{nome_modulo}' criado em modulos/{nome_modulo}.py")
else:
    print("ATENÇÃO!Esse módulo já existe!")
