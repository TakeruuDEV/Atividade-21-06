# Faça um programa que gere as tabuadas do 1 até o 10. 
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(i, "x", j, "=", i * j)
        j += 1
    i += 1