#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2017.2
#Professor: Fernando Ferraz Ribeiro
#Exemplo: Triângulo de Sierpinski (análogo 3d)


import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d, Brep
import ghpythonlib.components as ghcomp


# --- entradas
# raio (item, float)
# iterac (item, int)

#plano de trabalho
pl = rs.WorldXYPlane()
#decompondo o plano
o,vrx, vry, vrz = pl

#base da piramide
base = ghcomp.Polygon(pl,Raio,3,0.0)

#vertice superior da piramide
p1 = Point3d(Raio*vrz)+ Point3d(o)

#desenhando a piramide
piramide = ghcomp.ExtrudePoint(base,p1)

#listas auxiliares
lista1 = [piramide]
lista2 = []


#iterações
for i in range(iterac):
    # para cada piramide
    for j in lista1:
        #extrair os vertices
        vert = ghcomp.DeconstructBrep(j)[2]
        #para cada vertice
        for k in vert:
            # escalonar a piramide em direção ao vertice
            elemento = ghcomp.Scale(j,k,.5)[0]
            #olocar o elelemnto na lista
            lista2.append(elemento)
    # preparando listas para nova iteração
    lista1 = lista2
    lista2 = []
    
# mostrando os resultados
a = lista1
    
    