from modulos import analise

df = analise.carregar_csv("dados.csv")

#Média dos salários
media_salario = df["salario"].mean()
print(f"Média dos salários: {media_salario:.2f}")

#Idade máxima
idade_maxima = df["idade"].max()
print(f"Maior idade registrada: {idade_maxima}")

#Filtrar pessoas com salário acima de 3500
print("\n Pessoas salário acima de 3500:")
print(df[df["salario"] > 3500])
