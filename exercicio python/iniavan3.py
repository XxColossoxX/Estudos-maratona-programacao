nota = (float(input("Digite a nota de prova do aluno: ")))

if nota >= 0 and nota <= 4:
    print("Valor: Irregular")
elif nota >= 4.1 and nota <= 6:
    print("Valor: Regular")
elif nota >= 6.1 and nota <= 8:
    print("Valor: Bom")
elif nota >= 8.1 and nota <= 10.0:
    print("Muito bom!")
else:
    print("Digite uma nota válida!")