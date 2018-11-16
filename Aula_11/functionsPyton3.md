# Funções Definidas Pelo Usuário - Python3

## Algoritmo do cálculo da escada

### Algoritmo Original - Escada

```python
import math

# entrada do desnivel da escada
desnivel = float(input("entre com o desnível da escada \n"))
# entrada do espelho máximo
espMax = float(input("Digite o espelho máximo \n"))

# número de espelhos
nEsp = desnivel / espMax
# numero de espelhos arredondado
nEsp = math.ceil(nEsp)
# altura do espelho real
h = desnivel / nEsp
# altura do espelho com 3 casas decimais
h = round(h, 3)

# resultados:
## Número d espelhos
print("o número de espelhos é ", nEsp)
## medida dos espelhos
print("os espelhos tem altura de  ", h)

# calculo do piso pela formula de Blodel
piso = .63 - (2*h)

# resultado:
## medida do piso
print("o piso tem ", piso, "m")

```

### Transformando em função - Escada

imortando as dependências

```python
# dependencias
from math import ceil
```

definição da função

```python
# função
def Blondel(desnivel, espMax):

    # número de espelhos
    nEsp = desnivel / espMax

    # numero de espelhos arredondado
    nEsp = ceil(nEsp)

    # altura do espelho real
    h = desnivel / nEsp
    # altura do espelho com 3 casas decimais
    h = round(h, 3)
    # calculo do piso pela formula de Blodel
    piso = .63 - (2*h)
    # retorno da função
    return nEsp, h, piso
```

Chamada da função

```python
# chamada da função

result = Blondel(3.0, .18)

print(result)

```

## Nível dos pavimentos

### Algoritmo original - nível dos pavimentos

```python

nTerreo = float(input("Digite a cota do Terreo \n"))

pap = float(input("digite a cota de piso a piso \n"))

nPav = int(input("digite o numero de pavimentos \n"))

pavAtual = nTerreo

# loop for
for pav in range(nPav+1):
    print(" cota do pavimento", pav, "= ", pavAtual)
    # nova cota de pavimento
    pavAtual = pavAtual + pap
```

Função Cota dos pavimentos

```python
def PavNivel(nTerreo, pap, nPav):
    pavAtual = nTerreo
# loop for
    lNivel = []
    for pav in range(nPav+1):
        lNivel.append(pavAtual)
        # nova cota de pavimento
        pavAtual = pavAtual + pap

    return lNivel
```

Chamada da função

```python
# chamada da função Npav

result = PavNivel(1.3, 3.2, 10)

print(result)
```