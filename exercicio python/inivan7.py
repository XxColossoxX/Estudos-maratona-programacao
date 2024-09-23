def fatorar_numero(n): #n é dado para exemplificar o codigo, que o valor colocado na função, operará desta forma
    fatores = [] #a lista dos valores primos
    divisor = 2 #o primeiro divisor da operação, o primeiro numero primo

    while n > 1:   #enquanto o numero for maior que 1, ja que qnd chegar em 1 significa que ele nao sera mais divisivel
        if n % divisor == 0: #verifica se o divisor ainda vai ser 2, ja que quando fatoramos, chega uma hora que o numero nao consegue mais dividir por dois
            fatores.append(divisor) #quando ele nao consegue mais dividir, ele manda pra lista fatores o divisor que foi usado
            n //= divisor #aqui faz com que a divisao ocorrida pelo divisor, nao fique em flutuante, passando assim para o valor abaixo, por exemplo, se na divisao der 7.5, por conta do codigo, diz que o resultado da divisao deu 7
        else:
            divisor += 1 #aqui faz com que , caso o divisor nao % == 0, aumente um valor para ser o divisor, ou seja, ele verifica se é possivel dividir pelo numero, caso nao, ele adiciona +1 ao divisor, até ser possivel dividir 

    return fatores #aqui retorna todos os divisores que foram utilizados e guardados na lista do fatores

numero = (int(input("Digite um numero que será fatorado: ")))
print(f"Fatores primos de {numero}: {fatorar_numero(numero)}")