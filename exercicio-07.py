import pandas as pd

dados = {
    "NOME": ["Paulo", "Victor", "Wendel"],
    "IDADE": [18, 19, 20],
    "CIDADE": ["Camaçari", "Feira", "Itapiririca"]
}

dF = pd.DataFrame(dados)
print(dF)

for dado in dF.values:
    # print(dado)
    print(dado[0], dado[1], dado[2])