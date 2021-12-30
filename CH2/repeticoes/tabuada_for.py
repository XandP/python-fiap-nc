numero = int(input("Digite um número para exibir a tabuada dele: "))

for fator_multiplicativo in range(1,11,1):
    print(str(numero) + " x " + str(fator_multiplicativo) + " = " + str(numero*fator_multiplicativo))