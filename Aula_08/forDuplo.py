#! python
#! -*-encoding-:- utf8

# criando listas
lista1 = range(0,3,1)
lista2 = ['a', 'b', 'c', 'd']

#exibindo lista1
print 'lista 1: ',lista1

# exibindo lista2
print 'lista 2: ', lista2

#pular linha
print '\n'
#mensagem de início do primeiro loop
print 'inicio do primeiro for \n'
listaXY = [] # iniciando lista vazia
for i in range(len(lista1)): # prineiro for
    listaAux = [] # iniciando lista auxiliar
    print 'loop ', i , ' do primeiro for' # 
    for j in range(len(lista2)):
        pTemp = 'P(' + str(lista1[i]) + ',' + lista2[j] + ')' #criando ponto
        listaAux.append(pTemp) #Adicionando ponto na lista auxiliar
        listaXY.append(listaAux) #Adicionando lista auxiliar na listaXY
    print listaXY, "\n" # mostrando listaXY
    
    
