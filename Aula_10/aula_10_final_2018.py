#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2018.2
#Professor: Fernando Ferraz Ribeiro
#Exemplo pavimentos multiplos


import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d, Vector3d, Plane

if P2D is None:
    P2D = Plane((0,0,0), (1,0,0), (0,1,0))
if rs.IsPoint(P2D):
    P2D = Plane(P2D,(1,0,0), (0,1,0))

if P3D is None:
    P3D =  Plane((0,0,0), (1,0,0), (0,1,0))
if rs.IsPoint(P3D):
    P3D = Plane(P3D,(1,0,0), (0,1,0))


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
print P2D
print P3D


#função principal

# - criando uma face atravez das curvas de contorno
face = rs.AddPlanarSrf(Contorno)
# - ponto auxiliar para extrusão da face
Paux = P3D.Origin + Point3d(0,0,h_laje)
# linha auxiliar para a extrusão da face
lAux = rs.AddLine(P3D.Origin, Paux)

# - extrusão da face - criação da laje
laje = rs.ExtrudeSurface(face,lAux )

# - movendo laje do ponto 2d para o ponto 3d

laje = rs.OrientObject(laje, (P2D.Origin, P2D.XAxis, P2D.YAxis), 
                             (P3D.Origin, P3D.XAxis, P3D.YAxis)
)


#criando multiplos andares
for i in range(N_andares +1):
    # calculando altura do pavimento
    zAux = P3D.OriginZ + (i *PD) 
    # criando ponto na altura do pavimento
    pAux = Point3d(P3D.OriginX, P3D.OriginY, zAux)
    # vetor auxiliar para mover o pavimento
    vecAux2 = rs.VectorCreate(pAux, P3D.Origin)
    # saida de teste para o vetor vecaux
    #Teste.append(vecAux2)
    # copiando laje para altura do pavimento
    ljAux = rs.CopyObject(laje, vecAux2)
    # rotacionando laje
    ljAux = rs.RotateObject(ljAux, P3D.Origin, Rot*i, P3D.ZAxis )
    #colocando laje na saida dos pavimentos
    Pav.append(ljAux)
    
# --- FIM
