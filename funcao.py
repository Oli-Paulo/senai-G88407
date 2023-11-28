#Função para descobrir idade.
def idadeUsuario(idade):

    if idade >= 0 and idade <= 13:
        print("Você é uma criança.")
    elif idade > 13 and idade < 18:
        print("Tu é um adolescente.")
    elif idade >= 18 and idade < 60:
        print("Tu é um adulto.")
    elif idade >= 60:
        print("Tu é um velho.")

#Função booleana
def boolHumano(humano):

    if humano == "SIM":
        humano == True
        print("Tu é um humano")
    else:
        humano == False
        print("Tu não é um humano")

#Função para calcular custo de viagem
def calcularCustoViagem(distancia, tipo_veiculo):

    if tipo_veiculo == "CARRO":
        custo_por_km = 0.5

    elif tipo_veiculo == "MOTO":
        custo_por_km = 0.2

    elif tipo_veiculo == "BICICLETA":
        custo_por_km = 0.1
    
    else:
        print("Tipo de vaículo inválido.")
        return None

    custo_total = distancia * custo_por_km
    return custo_total