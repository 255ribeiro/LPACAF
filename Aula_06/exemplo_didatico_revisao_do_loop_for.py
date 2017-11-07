import rhinoscriptsyntax as rs

# loop for
for i in range(5):
    # a cada passagem do loop a variável c1 recebe o valor
    # do ultimo circulo criado
    # os valores anteriores são apagados
    c1 = rs.AddCircle([i,0,0],i+1)

# desta maneira apenas o ultimo círculo é extrudado
linAux = rs.AddLine([0,0,0],[0,0,5])
tubo = rs.ExtrudeCurve(c1,linAux)