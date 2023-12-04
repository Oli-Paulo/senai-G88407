#Menu McDonalds
from turtle import clear


def exibirMenu(cardapio):
    for lanches, preco in cardapio.items():
        print(lanches, preco)
    return True

def adicionarPedido(pedido):
    while True:
        itemPedido = input("Digite o número do pedido que você deseja. (ou 's' para sair):")
        if itemPedido.lower() == "s":
            return True
        elif int(itemPedido) == 1:
            pedido["BigMac"] = 30.00

        elif int(itemPedido) == 2:
            pedido["BigTasty"] = 33.00

        elif int(itemPedido) == 3:
            pedido["Refri"] = 9.00

        elif int(itemPedido) == 4:
            pedido["Milk Shake"] = 12.00

        elif int(itemPedido) == 5:
            pedido["Batata frita M"] = 7.00
        
        else:
            print("Informação não encontrada.")

def removerPedido(pedido):
    while True:
        itemPedido = input("Digite o número do pedido que você deseja retirar. (ou 's' para sair):")
        if itemPedido == "s":
            return True
        elif int(itemPedido) == 1:
            pedido.pop("BigMac")

        elif int(itemPedido) == 2:
            pedido.pop["BigTasty"] = 33.00

        elif int(itemPedido) == 3:
            pedido.pop["Refri"] = 9.00

        elif int(itemPedido) == 4:
            pedido.pop["Milk Shake"] = 12.00

        elif int(itemPedido) == 5:
            pedido.pop["Batata frita M"] = 7.00
        
        else:
            print("Informação não encontrada.")


def exibirPedido(pedido):
    for lanches, preco in pedido.items():
        print(lanches, preco)
    return True

def totalPedido(pedidoTotal):
    totalPedido = sum(pedidoTotal.values())
    print(f"O total do seu pedido é igual a: R${totalPedido}")
    return True 

def encerrarPrograma():
    print("Obrigado por escolher a nossa lanchonete, bom lanche e volte sempre.")

menu = {
    "1.BigMac:": "R$30,00",
    "2.BigTasty:": "R$33,00",
    "3.Refri:": "R$9,00",
    "4.Milk Shake:": "R$12,00",
    "5.Batata frita M:": "R$7,00"
}

pedido = {

}

status = True
while status == True:
    opcoes = input("""
    ===============================================\n
    1.Cardápio  2.Fazer pedido  3.Remover pedido\n
     4.Exibir pedido  5.Calcular Total  6.Sair\n
    ===============================================
    """)

    if opcoes == "1":
        status = exibirMenu(menu)

    elif opcoes == "2":
        status = adicionarPedido(pedido)
    
    elif opcoes == "3":
        status = removerPedido(pedido)

    elif opcoes == "4":
        status = exibirPedido(pedido)

    elif opcoes == "5":
        status = totalPedido(pedido)
        
    elif opcoes == "6":
        status = encerrarPrograma()
    
    else:
        print("Opção não encontrada.")
        status = True
