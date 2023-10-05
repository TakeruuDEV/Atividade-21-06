peso = float(input("Qual é o seu peso (em kg)? "))
altura = float(input("Qual é a sua altura (em metros)? "))

imc = peso / (altura ** 2)

if imc < 18.5:
  print("Abaixo do peso")
elif imc < 25:
  print("Peso normal")
elif imc < 30:
  print("Acima do peso")
elif imc < 35:
  print("Obesidade grau I")
else:
  print("Obesidade grau II ou III")
