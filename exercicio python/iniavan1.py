print("CALCULADORA DE IMC")
peso = (float(input("Digite seu peso em (KG): ")))
altura =(float(input("Digite sua altura em (M): ")))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25.0 and imc <= 29.9:
    print("Excesso de peso")
elif imc >= 30.0 and imc <= 34.9:
    print("Obesidade classe I")
elif imc >= 35 and imc <= 39.9:
    print("Obesidade classe II")
elif imc >= 40:
    print("Obesidade classe III")
else:
    print("Digite um IMC válido")

