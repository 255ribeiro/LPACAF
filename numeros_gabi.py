#! python3

file = open('NumerosGabi.txt','w')

inicio = int(input('digite o início da contagem:\n'))



final = int(input('digite o final da contagem:\n'))
final = final + 1


for i in range(inicio, final):
    file.write(str(i)+ ' ')

file.close()

input('pess any key')


