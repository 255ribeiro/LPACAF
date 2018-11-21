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

### Transformando em função - Malha Irregular

```python




```

## Edfício de Multiplos pavimentos

### Algoritmo Original - Edfício de Multiplos pavimentos

```python




```

### Transformando em função - Edfício de Multiplos pavimentos

```python




```
