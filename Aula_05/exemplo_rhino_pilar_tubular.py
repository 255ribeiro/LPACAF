import rhinoscriptsyntax as rs

print "desenhando um circulo"
# permite ao usuario clicar em um ponto
# o ponto e armazenado na variavel pt1
pt1 = rs.GetPoint("digite o ponto central")

# permite ao usuario entrar com o valor do raio
raio = rs.GetReal("entre com o raio", number= 1)
#desenha um circulo com o ponto e o raio definidos pelo usuario
c1 = rs.AddCircle(pt1,raio)
#pede que o usuario entre com a altura do pilar
h = rs.GetReal("entre com altura", number= 1)
# cria uma lista com as coordenadas do ponto pt1 somado a altura h
pt2 = rs.PointAdd(pt1, [0,0,h])
print pt2
#cria um ponto com as coordenadas de pt1 + a altura h
pt2 = rs.AddPoint(pt2)
print pt2
# linha auxiliar para a extrusao
linAux = rs.AddLine(pt1,pt2)
# extrusao de uma superficie aberta
tubo = rs.ExtrudeCurve(c1, linAux)
# fechando o objeto
rs.CapPlanarHoles(tubo)



