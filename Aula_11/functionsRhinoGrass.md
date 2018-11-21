# Funções Definidas Pelo Usuário - Rhino/Grasshopper

## Função pilares tubulares

```python

# dependencias
import rhinoscriptsyntax as rs

# Função
def PilaresTubulares(pointList1, pointList2, Raio, capTipo = 1):
    eixos =[]
    pilares = []
    for i in range(len(pointList1)):
        #criando linhas de eixos
        linAux = rs.AddLine(pointList1[i],pointList2[i])
        eixos.append(linAux)
        # criando pilares
        if Raio != 0:
            tubo = rs.AddPipe(linAux, 0, Raio, cap = capTipo)
            pilares.append(tubo)
    #retorna eixos e pilares
    return eixos, pilares


```

## Plano por superfície

```python
#dependencias
from Rhino.Geometry import Point3d, Vector3d, Plane, Surface

# Função
# sur1 superfície plana
def planoSuperf(sur1):
    auxPlane = Plane(sur1.PointAt(0,0), Vector3d(sur1.PointAt(1,0) - sur1.PointAt(0,0)) , Vector3d(sur1.PointAt(0,1) - sur1.PointAt(0,0) ) )
    return auxPlane

```

## Mudança de planos -  único objeto

```python
#dependencias
import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d, Vector3d, Plane

#função
# objeto1 -> geometria a ser moviva, plano1 -> plano de referencia, plano2 plano de destino
def MudaPlano(objeto1, plano1, plano2):
    objeto2 = rs.OrientObject(objeto1,
    [plano1.Origin,  Point3d(plano1.Origin + plano1.XAxis),  Point3d(plano1.Origin + plano1.YAxis)],
    [plano2.Origin, Point3d(plano2.Origin + plano2.XAxis), Point3d(plano2.Origin + plano2.YAxis)])
    return objeto2
```

## Mudança de planos - multiplos objetos

```python
#dependencias
import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d, Vector3d, Plane

#função
# objeto1 -> lista de geometrias a ser moviva, plano1 -> plano de referencia, plano2 plano de destino
def MudaPlanoLista(objetos, plano1, plano2):
    objetos2=[]
    for objeto in objetos:
        objeto2 = rs.OrientObject(objeto,
        [plano1.Origin,  Point3d(plano1.Origin + plano1.XAxis),  Point3d(plano1.Origin + plano1.YAxis)], [plano2.Origin, Point3d(plano2.Origin + plano2.XAxis), Point3d(plano2.Origin + plano2.YAxis)])
        objetos2.append(objeto)
    return objetos2
```

## Malha Irregular

```python
# dependências
import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d, Vector3d, Plane

#função
def ManhaIrregular(PL, Lx, Ly, sX = 0.0, sY = 0.0):
    P =[]

# - função principal
    Lx.insert(0, 0.0)
    Ly.insert(0, 0.0)
# - mudando a origem x e y do plano
    PL.OriginX = PL.OriginX + sX
    PL.OriginX = PL.OriginX + sY

    tempX = 0
    for x in range(len(Lx)):
        tempX = tempX + Lx[x]
        tempY = 0
        for y in range(len(Ly)):
            tempY = tempY + Ly[y]
            pTemp = PL.Origin + (tempX *  PL.XAxis) +  (tempY * PL.YAxis)
            P.append(pTemp)
    return P

```