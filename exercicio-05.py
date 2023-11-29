Usuarios = {
    "PAULO": 12345,
    "VICTOR": 54321,
    "ALAN": 67890
}

nome = input("Nome do usuário: ").upper()
senha = int(input("Senha do usuário: "))

if nome in Usuarios and Usuarios[nome] == senha:
    print("Usuário e senha corretos!")
else:
    print("Usuário ou senha inválidos!")
