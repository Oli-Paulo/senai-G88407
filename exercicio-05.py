def login(dicionario):
    nome = input("Nome do usuário: ")
    senha = int(input("Senha do usuário: "))

    if nome in Usuarios and Usuarios[nome] == senha:
        print("Usuário e senha corretos!")
        return True
    else:
        print("Usuário ou senha inválidos!")
        return True

def criarUsuario():
        criarUsuario = input("Nome desejado: ")
        criarSenha = int(input("Crie a senha apenas com números: "))
        Usuarios[criarUsuario] = criarSenha
        return True


Usuarios = {
    "Paulo": 12345,
    "Victor": 54321,
    "Alan": 67890
}

status = True
while status == True:
    opcoes = input("""
    Escolha a opção desejada:\n
    1 = Login  2 = Criar conta  3 = sair
    """)

    if opcoes == "1":
        status = login(Usuarios)

    elif opcoes == "2":
        status = criarUsuario()
    
    elif opcoes == "3":
        print("Obrigado por acessar!")       
        status = False

    else:
        print("Opção não encontrada.")
        status = True
