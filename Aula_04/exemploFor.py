# coding= utf8
# Variável que controla o tamanho das listas
# troque valor de tl para mudar o tamanho das listas
tl = 4

# criando as listas
lista1 = range(0, (2*tl), 2)
lista2 = range(1, ((2*tl)+1), 2)

# mostrando o tamanho das listas
print "lista 1 contem ", len(lista1), "elementos"
print "lista 2 contem ", len(lista2), "elementos"

# mostrando as listas
print " lista 1 :\n", lista1
print " lista 2 :\n", lista2

# armazenando o tamanho da lista 1 na variavel tam
tam = len(lista1)
print "valor da variável tam = ", tam

# usando o comando range e a variavel tam
# para montar uma lista com os indices da lista 1
indices = range(tam)
# mostrando a lista de indices
print "lista de indices", indices

print "percorrendo a lista de indices"
# percorrendo a lista de indices com o comando for
for elemento in indices:
    print "elemento =", elemento

print "Combinando os valores de indices iguais das duas listas "
# combinando duas listas de mesmo tamanho com o comando for
for i in range(4):
    print lista1[i], "-", lista2[i]
print " fim do programa"
# raw_input("pressione enter para sair")
