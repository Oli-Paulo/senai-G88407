import funcao

Nome = "Paulo Eduardo Santos Oliveira"
Idade = 20
Altura = 1.78
Estudante = True

print("""
Nome = {}
Idade = {}
Altura = {}
Estudante = {}
""".format(type(Nome), type (Idade), type (Altura), type (Estudante)))

soma = 5 + 3
sub = 5 - 3
mult = 5 * 3
divi = 5 / 3
print("Operadores matemáticos: Soma = ", soma, "Subtração = ", sub,
"Multiplicação = ", mult, "Divisão = ", divi)

Igual = 5 == 3
Difer = 5 != 3
Maior = 5 > 3
Menor = 5 < 3
print("Operadores de comparação: Igualdade = ", Igual, "Diferença = ", Difer,
"Maior = ", Maior, "Menor = ", Menor)

E = True and False
OU = True or False
NAO = not True
print("Operadores lógicos: E = ", E, "Ou = ", OU,
"Não = ", NAO)