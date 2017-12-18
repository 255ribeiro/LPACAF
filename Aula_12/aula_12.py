#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2017.1
#Coordenador: Arivaldo Leão de Amorim
#Professor: Fernando Ferraz Ribeiro
#Exemplo: perfis da treliça pelos euxos dos banzos

#Importando Módulos
import rhinoscriptsyntax as rs

#--- Entradas:
#Eixo -- (item, ghdoc)
#Ex Curva do banzo inferior -- (item, float)
#Ey -- (item, float)


#saidas

# Lista com as barras quadradas
Barras = []

vrZ = rs.VectorCreate([0,0,-1], [0,0,0])

normal = rs.CurveTangent(Eixo, 0)

vecBase = rs.VectorCrossProduct(vrZ, normal)

plAux = rs.PlaneFromNormal (rs.CurveStartPoint(Eixo), normal, xaxis=vecBase)
print plAux

o1, x1, y1, z1 = plAux

vAux = rs.VectorAdd((-Ex/2)*x1, (-Ey/2)*y1)

o2 = rs.PointAdd(o1, vAux)

plAux = rs.MovePlane(plAux, o2)

perfil = rs.AddRectangle(plAux, Ex, Ey)

elemento = rs.AddSweep1(Eixo, [perfil])

rs.CapPlanarHoles(elemento)

Barras = elemento


vecTeste = rs.VectorCrossProduct(-normal , normal)

print vecTeste