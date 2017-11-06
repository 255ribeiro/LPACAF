import rhinoscriptsyntax as rs

print "Pilar Circular - Extrude"

## Entradas
# permite ao usuario clicar em um ponto
# o ponto e armazenado na variavel pt1
pt1 = rs.GetPoint("digite o ponto central")

# permite ao usuario entrar com o valor do raio
raio = rs.GetReal("entre com o raio", number= 1)

#pede que o usuario entre com a altura do pilar
h = rs.GetReal("entre com altura", number= 1)

#desenho
#desenha um circulo com o ponto e o raio definidos pelo usuario
c1 = rs.AddCircle(pt1,raio)
# cria uma lista com as coordenadas do ponto pt1 somado a altura h
pt2 = rs.PointAdd(pt1, [0,0,h])

# linha auxiliar para a extrusao
linAux = rs.AddLine(pt1,pt2)
# extrusao de uma superficie aberta
tubo = rs.ExtrudeCurve(c1, linAux)
# fechando o objeto
rs.CapPlanarHoles(tubo)



