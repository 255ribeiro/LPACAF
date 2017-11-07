import rhinoscriptsyntax as rs

print "Pilar Circular Utilizando o Comando Pipe"

## Entradas
# permite ao usuario clicar em uma curva
# a curva e armazenado na variavel curva1
curva1 = rs.GetCurveObject("selecione uma curva", preselect = True, select = True)

# permite a entrada de um numero inteiro que determina
# em quantos segmentos sera dividida a curva1
# armazena o numero inteiro na variavel numP
numP = rs.GetInteger("entre com o numero de divisoes", number = 10)
# permite ao usuario entrar com o valor real (float) do raio
raio = rs.GetReal("entre com o raio", number= 1)

#pede que o usuario entre com o valor real (float) da altura do pilar
h = rs.GetReal("entre com altura", number= 3)

## Desenho

#divide a curva1 em 
pLista = rs.DivideCurve(curva1[0],numP)

for pt in pLista:
    # cria um ponto com as coordenadas do ponto pt somado a altura h
    pt2 = rs.PointAdd(pt, [0,0,h])
    # linha auxiliar para a o comando pipe
    linAux = rs.AddLine(pt,pt2)
    # Desenhando o tubo
    tubo = rs.AddPipe(linAux, 0, raio, cap=1)




