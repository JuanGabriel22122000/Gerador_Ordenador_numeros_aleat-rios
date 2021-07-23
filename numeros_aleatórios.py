import random

def gerar_numero():
    arquivo = open("numeros.txt","w")

    contador = 0

    while(contador<=1000):
        numero = random.randrange(-50,1000)
        arquivo.write("{} ".format(numero))
        contador += 1

    arquivo.close