# programa para calcular el IMC
peso = float(input("peso (kg): "))
altura = float(input("altura (m): "))
imc = peso / (altura ** 2)
print("su IMC es:", imc)