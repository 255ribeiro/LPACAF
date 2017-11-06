import rhinoscriptsyntax as rs

print "Pilar Circular Utilizando o Comando Pipe"

## Entradas
# permite ao usuario clicar em um ponto
# o ponto e armazenado na variavel pt1
pt1 = rs.GetPoint("digite o ponto central")

# permite ao usuario entrar com o valor do raio
raio = rs.GetReal("entre com o raio", number= 1)

#pede que o usuario entre com a altura do pilar
h = rs.GetReal("entre com altura", number= 3)

## Desenho

# cria uma lista com as coordenadas do ponto pt1 somado a altura h
pt2 = rs.PointAdd(pt1, [0,0,h])
# linha auxiliar para a o comando pipe
linAux = rs.AddLine(pt1,pt2)
# Desenhando o tubo
tubo = rs.AddPipe(linAux, 0, raio, cap=1)




