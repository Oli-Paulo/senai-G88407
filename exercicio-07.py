import pandas as pd

produtos = {
    "MESES": ["janeiro", "fevereiro", "março", "janeiro", "fevereiro", "março"],
    "PRODUTOS": ["Xiaomi", "iPhone", "Samsung", "Huawei", "Nokia", "Motorola"],
    "VENDAS": [22, 35, 40, 64, 85, 78]
}

dF = pd.DataFrame(produtos)
#print(dF)


dF2 = dF.set_index("MESES")
filtroMeses = dF2.loc[input("Escreva o mês em que você deseja ver os dados: ").lower()]
print(dF2)
print(filtroMeses)

vendas = dF.set_index("MESES")
filtroMeses = dF2.loc[input("Escreva o mês em que você deseja ver os dados: ").lower()]
