#Curso de Extensão:
#Lógica de programação aplicada à criação e análise da forma
#UFBa - Faculdade de Arquitetura - 2017.2
#Professor: Fernando Ferraz Ribeiro
#Exemplo treliça a partir dos eixos dos banzos

#Importando Módulos
import rhinoscriptsyntax as rs

#entradas

#--- Entradas:
#C1 Curva do banzo superior -- (item, ghdoc)
#C2 Curva do banzo inferior -- (item, ghdoc)
if type(C2) == float:
    C2 = rs.CopyObject(C1,[0,0,-C2])
#N1 Número de subdivisões dos banzos -- (item, int)
if not N1:
    N1 = 10


#Saidas
teste=[]
Cordas =[]
Diag =[]
Bsup =[]
Binf = []

## Gerando lista de pontos

# funcao DivideCurve recebe uma curva e divide em um numero de partes iguais N1
# retorna os pontos que dividem a curva
# equivante ao comando divide no rhino
pontosC1 = rs.DivideCurve(C1,N1)
pontosC2 = rs.DivideCurve(C2,N1)

## Banzos Retificados

# funcao polyline desenha uma polyline atravez dos pontos de uma lista
# respeitando a ordem dos indices

# Lista de pontos do banzo C1
Bsup = rs.AddPolyline(pontosC1)
# Lista de pontos do banzo C2
Binf = rs.AddPolyline(pontosC2)


## desenhando as cordas

# para cada elemento na listas de incices
for i in range(len(pontosC1)):
    # desenhar uma linha entre os pontos de indices correspondente de cada lista
    L1 = rs.AddLine(pontosC1[i], pontosC2[i])
    # colocando elemento na saida Cordas
    Cordas.append(L1)
    
    
## desenhando as diagonais

# criando listas auxiliares vazias apra serem preenchidas durante o for
lAux1 = []
lAux2 =[]


for i in range(len(pontosC1)):
    # se o indice do ponto e par:
    if i%2 == 0:
        # colocar pondo da lista de C1 na lista lAux2, usada para o dessenho...
        # ...da diagonal começando pelo banzo superior
        lAux2.append(pontosC1[i])
        # colocar pondo da lista de C2 na lista lAux1, usada para o dessenho...
        # ...da diagonal começando pelo banzo inferior
        lAux1.append(pontosC2[i])
    else:
        # colocar pondo da lista de C2 na lista lAux2, usada para o dessenho...
        # ...da diagonal começando pelo banzo supeiror
        lAux2.append(pontosC2[i])
        # colocar pondo da lista de C1 na lista lAux1, usada para o dessenho...
        # ...da diagonal começando pelo banzo inferior
        lAux1.append(pontosC1[i])

# colocando as diagonais na lista de saida Diag

## Tipo de Treliça
# a variavel Tipo determina como as diagonais serao desenhadas:
#       0 - não desenha diagonais
#       1 - desenha diagonais começando do banzo inferior
#       2 - desenha diagonais começando no banzo superior
#       3 - desenha diagoanis cruzadas


# se a varíavel tipo não for informada
if Tipo is None:
    Tipo =1
# se tipo == 1
if Tipo == 1:
    # diagonais partindo do banzo inferior (início da lista)
    Diag = rs.AddPolyline(lAux1)
    # se tipo == 2
elif Tipo == 2:
    # diagonais partindo do banzo superior (início da lista)
    Diag = rs.AddPolyline(lAux2)
    # diagonais cruzadas
elif Tipo ==3:
    Diag = [rs.AddPolyline(lAux1), rs.AddPolyline(lAux2)]
    # tipo == 0
elif Tipo == 0:
    # não coloca nada na saida Diag
    pass
    
