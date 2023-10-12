"""Exercício de Desafio do Modulo 3 - Loops
FEA.dev - Python """

altura = -1
while altura<=0 or altura>8:
    altura = int(input("Qual a altura do Triângulo? (de 1 a 8): "))

for cada_linha in range(1, altura+1):
    print(" "*(altura-cada_linha), end="")
    print("#"*cada_linha)