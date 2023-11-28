import funcao

tipo_veiculo = input("Entre um carro, uma moto e uma bicicleta, com qual você preferiria viajar? ").upper()
distancia = float(input("Qual a distância que você quer viajar? "))

custo = funcao.calcularCustoViagem(distancia, tipo_veiculo)

print(custo)