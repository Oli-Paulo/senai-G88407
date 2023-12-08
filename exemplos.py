#Media de notas.
notas = [90,85,78,92,88,76,95,89]
soma = 0
for nota in notas:
    soma += nota

media = soma/len(notas)
print("A média das notas é: ", media)

#Pandas
import pandas as pd

data = {
    "apples":[3,2,0,1],
    "oranges":[0,3,7,2]
}
tabela = pd.DataFrame(data)
print(tabela)

#Exemplo de pandas
dados = {
    "NOME": ["Paulo", "Victor", "Wendel"],
    "IDADE": [18, 19, 20],
    "CIDADE": ["Camaçari", "Feira", "Itapiririca"]
}

dF = pd.DataFrame(dados)
print(dF)

for dado in dF.values:
    # print(dado)
    print(dado[0])