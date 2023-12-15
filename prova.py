def autenticar(contas):
        senha = int(input("Senha do usuário: "))

        if contas["Senha"] == senha:
            print("Bem vindo.")
            return True
        else:
            return False

def verificar_saldo(contas):
    saldo = contas["Saldo"]
    print(f"Seu saldo é de R${saldo},00")
    return True

def depositar(contas):
    saldo = contas["Saldo"]
    deposito = int(input("Escreva o valor que deseja depositar."))
    soma = deposito + saldo
    print(f"Seu saldo agora é de R${soma},00")
    contas["Saldo"] = soma
    return True

def retirar(contas):
    saldo = contas["Saldo"]
    deposito = int(input("Escreva o valor que deseja retirar."))
    sub = saldo - deposito
    print(f"Seu saldo agora é de R${sub},00")
    contas["Saldo"] = sub
    return True

def sair():
    print("Obrigado por acessar.")

contas = {
    "Saldo": 90,
    "Senha": 12345
}

autenticacao = autenticar(contas)
print(autenticacao)

if autenticacao == True:
    status = True
    while status == True:
        menu = input("""
        ----------------------------------------\n
                    MENU DO CAIXA\n
        ----------------------------------------\n
        1.Verificar saldo  2.Depositar dinheiro\n
        3.Retirar dinheiro 4.Sair
        """)

        if menu == "1":
            status = verificar_saldo(contas)

        elif menu == "2":
            status = depositar(contas)

        elif menu == "3":
            status = retirar(contas)

        elif menu == "4":
            status = sair()

        else:
            print("Opção não encontrada.")
            status = True

else:
    print("Senha inválida!")