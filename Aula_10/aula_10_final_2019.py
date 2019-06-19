#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2018.2
#Professor: Fernando Ferraz Ribeiro
#Exemplo pavimentos multiplos


import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d, Vector3d, Plane, Point3dGrid

if P2D is None:
    P2D = Plane(Point3d(0,0,0), Vector3d(1,0,0), Vector3d(0,1,0))
if rs.IsPoint(P2D):
    P2D = Plane(P2D, Vector3d(1,0,0), Vector3d(0,1,0))

if P3D is None:
    P3D =  Plane(Point3d(0,0,0), Vector3d(1,0,0), Vector3d(0,1,0))
if rs.IsPoint(P3D):
    P3D = Plane(P3D, Vector3d(1,0,0), Vector3d(0,1,0))



#--- Entradas:
# P2D - ponto no desenho -- (item, Plane)
# P3D - ponto no terreno -- (item, Plane)
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

# gerando superfície atravès das linhas de contorno
face = rs.AddPlanarSrf(Contorno)
# ponto auxiliar para criaçao da diretriz da extrusão
pAux = P3D.Origin + Point3d( 0,0, h_laje)
# linha diretriz da extrusão
lAux = rs.AddLine(P3D.Origin, pAux)
# sólido gerado pela extrusão
laje = rs.ExtrudeSurface(face, lAux)


# alinhando com o plano P3D
laje = rs.OrientObject(laje, 
[P2D.Origin,  Point3d(P2D.Origin + P2D.XAxis),  Point3d(P2D.Origin + P2D.YAxis)], 
[P3D.Origin, Point3d(P3D.Origin + P3D.XAxis), Point3d(P3D.Origin + P3D.YAxis)])

# loop dos andares
for i in range(N_andares):
    # copiando laje de acordo com o vetor da altura dos pavimentos
    laje_aux = rs.CopyObject(laje, (i * PD *P3D.ZAxis) )
    # dotacionando pavimentos
    laje_aux = rs.RotateObject(laje_aux , P3D.Origin , (Rot * i/N_andares), P3D.ZAxis)
    # colocando laje do pavimento na lista de saida PAV
    Pav.append(laje_aux)