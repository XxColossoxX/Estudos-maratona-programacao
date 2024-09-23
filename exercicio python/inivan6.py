decimal = (int(input("Digite um numero decimal: ")))

conversaoresto1 = int(decimal % 2 )
conversaovalor1 = int(decimal / 2 )
conversaoresto2 = int(conversaovalor1 % 2)
conversaovalor2 = int(conversaovalor1 / 2)
conversaoresto3 = int(conversaovalor2 % 2)
conversaovalor3 = int(conversaovalor2 / 2)
conversaoresto4 = int(conversaovalor3 % 2)


print(conversaoresto4,conversaoresto3,conversaoresto2,conversaoresto1)
#tem que ser ao contrario, já que a colocação de decimal para binário
#se faz do ultimo resto, até o primeiro resto


binario = bin(decimal)[2:] #objeto bin()tranforma o valor em binario 
#                      ^^ faz com que pule dois numeros. Teste sem ele para entender

print(binario)