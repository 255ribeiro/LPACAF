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

## Função treliça

```python




```

## Malha Regular

```python




```

## Malha Irregular

```python




```

## Mudança de planos

```python
#dependencias
import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d, Vector3d, Plane

#função

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

def MudaPlanoLista(objetos, plano1, plano2):
    objetos2=[]
    for objeto in objetos:
        objeto2 = rs.OrientObject(objeto,
        [plano1.Origin,  Point3d(plano1.Origin + plano1.XAxis),  Point3d(plano1.Origin + plano1.YAxis)], [plano2.Origin, Point3d(plano2.Origin + plano2.XAxis), Point3d(plano2.Origin + plano2.YAxis)])
        objetos2.append(objeto)
    return objetos2
```