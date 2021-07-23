#lista de saida de dados

def ordenar_numeros():
    lista = []

    with open('numeros.txt','r') as numero:
        conteudo = numero.read()
        numeros = conteudo.split()

        for nub in numeros:
            conversor = int(nub)
            lista.append(conversor)

        ref = len(numeros) 
        contador = 0
        lista_saida = []

        while(contador < ref):
            indice = lista.index(max(lista))
            lista_saida.append(lista.pop(indice)) 
            contador +=1



    arquivo = open("numeros_ordenados.txt", "w")

    for conversor in lista_saida:
        arquivo.write("{} ".format(conversor))

    arquivo.close

