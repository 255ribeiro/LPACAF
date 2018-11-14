# Funções Definidas Pelo Usuário

## Algoritmo do cálculo da escada

### Algoritmo Original - Escada

```python
import math

# entra do desnivel da escada
desnivel = float(input("entre com o desnível da escada \n"))

espMax = float(input("Digite o espelho máximo \n"))

# número de espelhos
esp = desnivel / espMax

# numero de espelhos arredondado
esp = math.ceil(esp)

print(esp)

# altura do espelho real
h = desnivel / esp
# altura do espelho com 3 casas decimais
h = round(h, 3)

# resultados:
## Número d espelhos
print("o número de espelhos é ", esp)
## medida dos espelhos
print("os espelhos tem altura de  ", h)

# calculo do piso pela formula de Blodel
piso = .63 - (2*h)

# resultado:
## medida do piso
print(" o piso tem ", piso, "m")


```

### Transformando em função - Escada

```python




```

## Pilares tubulares

### Algoritmo Original - pilares tubulares

```python




```

### Transformando em função - pilares tubulares

```python




```

## Treliça

### Algoritmo Original - treliça

```python




```

### Transformando em função - treliça

```python




```

## Malha Regular

### Algoritmo Original - Malha Regular

```python




```

### Transformando em função - Malha Regular

```python




```


## Malha Irregular

### Algoritmo Original - Malha Irregular

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
