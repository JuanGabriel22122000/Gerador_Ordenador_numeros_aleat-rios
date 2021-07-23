lista = []
with open('numeros.txt','r') as numero:

    conteudo = numero.read()
    numeros = conteudo.split()

    for nub in numeros:
        conversor = int(nub)
        lista.append(conversor)

    
print(type(lista[0]))

