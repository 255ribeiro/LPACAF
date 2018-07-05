#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2017.2
#Professor: Fernando Ferraz Ribeiro
#Exemplo Malha de ponto Irregular

#--- Importando modulos
import rhinoscriptsyntax as rs
 
#--- Entradas:
#O origem da malha -- (item, ghdoc)
#Lx Listas de vãos no sentido x -- (list, float)
#Ly Listas de vãos no sentido y -- (list, float)


if O is None:
    O = rs.AddPoint([0,0,0])

# saidas
P =[]

# - função principal
# - função principal

Lx.insert(0,0.0)
Ly.insert(0,0.0)

# zerando variavel antes do loop
xAux = 0
for i in Lx:
    xAux = xAux + i
    # zerando variavel antes do loop
    yAux =0
    for j in Ly:
        #atualizando valor da variável 
        yAux = yAux + j
        print xAux, yAux, 0
        # cria novo ponto somando com o ponto de origem
        pt = rs.PointAdd(O,[xAux, yAux, 0])
        # coloca o ponto criado na lista de saidas p
        P.append(pt)