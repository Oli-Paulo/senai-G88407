from pickle import FALSE
from re import sub


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

Soma = 5 + 3
Sub = 5 - 3
Prod = 5 * 3
Divi = 5 / 3
print("Operadores matemáticos: Soma = ", Soma, "Subtração = ", Sub,
"Multiplicação = ", Prod, "Divisão = ", Divi)

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