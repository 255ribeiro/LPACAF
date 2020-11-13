#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2018.2
#Professor: Fernando Ferraz Ribeiro
#Exemplo pavimentos multiplos
from __future__ import print_function
import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d, Vector3d, Plane, Point3dGrid

if P2D is None:
    P2D = Plane(Point3d(0,0,0), Vector3d(1,0,0), Vector3d(0,1,0))


if P3D is None:
    P3D =  Plane(Point3d(0,0,0), Vector3d(1,0,0), Vector3d(0,1,0))

#--- Entradas:
# P2D - ponto no desenho -- (item, Plane)
# P3D - ponto no terreno -- (item, Plane)
# Contorno - contorno da laje -- (list, ghdoc)
# PD - distancia piso a piso-- (item, float)
# h_laje - altura da laje -- (item, float)
# N_andares - Numerod e andares y -- (item, int)
# Rot - rotação dos andares -- (item, float)

#Saidas
# listas de saida
pavConrotno = []
pavFace = []
pavLaje = []

#lista para teste de codigo
Teste = []

#função principal

# alinhando com o plano P3D
ContornoAux =[]

# orinetando os contornos
for curva in Contorno:
    ContornoOrient = rs.OrientObject(curva, 
    [P2D.Origin,  P2D.Origin + P2D.XAxis,  P2D.Origin + P2D.YAxis], 
    [P3D.Origin, P3D.Origin + P3D.XAxis, P3D.Origin + P3D.YAxis])
    ContornoAux.append(ContornoOrient)
    

# loop dos andares
for i in range(N_andares +1):
    
    ## Colocando os contornos na posição dos pavimentos
    
    #movendo o Contorno para a altura do pavimento
    ContornoPos = rs.CopyObjects(ContornoAux, (i * PD *P3D.ZAxis) )
    
    # rotacionando o contorno dos pavimentos
    ContornoPos = rs.RotateObjects(ContornoPos , P3D.Origin , (Rot * i/N_andares), P3D.ZAxis)

    ## Saida dos contornos
    # colocando o Contorno posicionado na lista de saida dos contornos
    pavConrotno  = pavConrotno + ContornoPos
    
    # Gerando superfície atravès das linhas de contorno
    face = rs.AddPlanarSrf(ContornoPos)
    
    ## Saida das faces
    # colocando a face na lista de saida das faces
    pavFace += face
    
    ## Gerando solidos
    # ponto auxiliar para criaçao da diretriz da extrusão
    pAux = P3D.Origin + Point3d( 0,0, h_laje)
    # linha diretriz da extrusão
    lAux = rs.AddLine(P3D.Origin, pAux)
    # sólido gerado pela extrusão

    lajeAux = rs.ExtrudeSurface(face, lAux)
    
    # saida das lajes
    # colocando laje do pavimento na lista de saida PAV
    pavLaje.append(lajeAux)