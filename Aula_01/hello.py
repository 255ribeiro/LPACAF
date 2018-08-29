#! python
from __future__ import division
import math as m

# entradas
des = input('entre com desnivel ')
espM = input('entre com o espelho maximo')

nEsp = m.ceil(des/espM)



#saida

print "Numero de espelhos = ", nEsp
 # arredondas
espR = round(des/nEsp, 3)

print 'espelho real ', espR

p = 63 - (2 * espR)

print "piso = ", p

raw_input('press any key')
