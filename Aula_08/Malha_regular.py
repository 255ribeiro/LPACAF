#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2017.2
#Professor: Fernando Ferraz Ribeiro
#Exemplo de malha regular de pontos

#importando modulos
import rhinoscriptsyntax as rs



# --- Entradas:
#Dx distância em x dos prontos da malha -- (item, float)
#Nx número de pontos da manha na direção x -- (item, int)
#Dy distância em y dos prontos da malha -- (item, float)
#Ny número de pontos da manha na direção y -- (item, int)



if  O is None:
    O = rs.AddPoint(0,0,0)


# --- Saidas

# Lista de pontos da malha de pilar
P= []

# eixos da manha na direção x
eixosX = []

# eios da malha na direção y
eixosY = []


# - Função principal

# lista auxiliar de pontos (sublistas para cada linha y)
Paux=[]

# loop for da dimensão x
for x in range(Nx):
    # lista auxiliar para cada linha de pontos
    LinAux =[]
    
    # loop for na dimensão Y
    for y in range(Ny):
        
        # cria pontos somando valores de coordenadas com a origem
        pt = rs.PointAdd(O, [x*Dx, y*Dy, 0])
        # coloca o ponto na lista auxiliar de linhas
        LinAux.append(pt)
    # coloca a lista linaux como uma sublista na lista Paxu
    Paux.append(LinAux)
    # concatena as listas linaux na lista da saida P
    P = P + LinAux
    
    # eixos no sentido Y
    # desenha uma linha entre os pontos exremos da lista linaux
    eixo = rs.AddLine(LinAux[0], LinAux[-1])
    eixosY.append(eixo)

# Eixos no sentido X
for i in range(Ny):
    
    # desenha loinha de eixo entre os pontos extremos da linha
    eixo = rs.AddLine(Paux[0][i], Paux[-1][i])
    # Coloca o eixo na lista de eixos X
    eixosX.append(eixo)


# --- Fim




