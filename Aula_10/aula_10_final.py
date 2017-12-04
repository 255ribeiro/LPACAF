#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2017.2
#Professor: Fernando Ferraz Ribeiro
#Exemplo pavimentos multiplos


import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d

if P2D is None:
    P2D = Point3d(0,0,0)


if P3D is None:
    P3D = Point3d(0,0,0)


#--- Entradas:
# P2D - ponto no desenho -- (item, Point3d)
# P3D - ponto no terreno -- (item, Point3d)
# Contorno - contorno da laje -- (list, ghdoc)
# PD - distancia piso a piso-- (item, float)
# h_laje - altura da laje -- (item, float)
# N_andares - Numerod e andares y -- (item, int)
# Rot - rotação dos andares -- (item, float)



#Saidas
# lista de pavimentos
Pav = []
#lista para teste de codigo
Teste = []


#função principal

# - criando uma face atravez das curvas de contorno
face = rs.AddPlanarSrf(Contorno)
# - ponto auxxiliar para extrusão da face
Paux = rs.PointAdd(P3D, [0,0,h_laje])
# linha auxiliar para a extrusão da face
lAux = rs.AddLine(P3D, Paux)

# - extrusão da face - criação da laje
laje = rs.ExtrudeSurface(face,lAux )

# - movendo laje do ponto 2d para o ponto 3d
# vetos auxiliar do movimento
vecAux = rs.VectorCreate(P3D, P2D)
# movendo lage
rs.MoveObject(laje,vecAux)


#criando multiplos andares
for i in range(N_andares +1):
    # calculando altura do pavimento
    zAux = P3D.Z + (i *PD) 
    # criando ponto na altura do pavimento
    pAux = Point3d(P3D.X, P3D.Y, zAux)
    # vetor auxiliar para mover o pavimento
    vecAux2 = rs.VectorCreate(pAux, P3D)
    # saida de teste para o vetor vecaux
    Teste.append(vecAux2)
    # copiando laje para altura do pavimento
    ljAux = rs.CopyObject(laje, vecAux2)
    # rotacionando laje
    ljAux = rs.RotateObject(ljAux, P3D, Rot*i, [0,0,1] )
    #colocando laje na saida dos pavimentos
    Pav.append(ljAux)
    
# --- FIM
