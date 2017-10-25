# coding= utf8

# Exemplos de loops while e for para ligar duas listas

# Criando a lista 1
lista1 = range(0, 10, 2)
# Criando a lista 2
lista2 = range(0, 10, 2)

# mostrando a lista 1
print "estado inicial da lista 1\n", lista1

# Critétio de parada do loop
# Mude o valor de parada para controlar o número de repetições
parada = 4

# iniciando o contador
count = 0

print "loop While"
# inicio do loop while
while count < parada:
    # retira o primeiro elemento da
    # lista1 e armazena na variavel x
    x = lista1.pop(0)
    # coloca a variável x no fim da lista 1
    lista1.append(x)
    # incrementa o contador
    count = count + 1
    # mostra o contador
    print "contador", count
    # estado parcial da lista
    print "estado parcial da lista 1", lista1

# fim do loop
print "Fim do loop while"
# estado final da lista
print "estado final da lista 1:\n", lista1

print "------------------------------------------"
# mostrando a lista 2
print " estado inicial da lista 2\n", lista2

print "loop for"
# inicio do loop for
for i in range(parada):
    # retira o primeiro elemento da
    # lista1 e armazena na variavel x
    x = lista2.pop(0)
    # Coloca a variável x no fim da lista 1
    lista2.append(x)
    # estado parcial da lista
    print "estado parcial da lista 2", lista2
# fim do loop
print "Fim do loop for"
# estado final da lista
print "estado final da lista 2:\n", lista2
print " fim do programa"
# raw_input("pressione enter para sair")
