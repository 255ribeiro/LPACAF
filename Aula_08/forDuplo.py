#! -*-coding-:- utf8

# criando listas
lista1 = range(0,5,1)
lista2 = ['a', 'b', 'c', 'd']

#exibindo lista1
print lista1

# exibindo lista2
print lista2

#mensagem
print 'inicio do for'

listaXY = [] # iniciando lista vazia
for i in range(len(lista1)): # prineiro for
    listaAux = [] # iniciando lista auxiliar
    print 'loop ', i , ' do primeiro for \n'
    for j in range(len(lista2)):
        pTemp = 'P(' + str(lista1[i]) + ',' + lista2[j] + ')' #criando ponto
        listaAux.append(pTemp) #Adicionando ponto na lista auxiliar
        listaXY.append(listaAux) #Adicionando lista auxiliar na listaXY
    print listaXY # mostrando listaXY
