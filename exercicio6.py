# Faça um programa em que o usuário digita um número inteiro e o programa exibe todos os números ímpares do 1 até o valor inserido.
n = int(input("Digite um número: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)

n = int(input("Digite um número: "))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1