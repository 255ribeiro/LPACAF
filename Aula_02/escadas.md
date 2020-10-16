# Cálculo de escadas pela fórmula de Blondel

## Estabelecer uma sequência de passos para calcular o piso e o espelho de uma escada em função do desnível e de um valor de espelho máximo.

### Condições adicionais:

1. Todos os degraus devem ter a mesma altura de espelho e a mesma medida de piso.
2. A medida da altura do espelho deve ser a maior possível, sem exceder a altura máxima indicada.

### Relenbrando a formula de Blondel:


<img src="https://latex.codecogs.com/svg.latex?\Large&space;2\times{h} + p = 63cm" title="2\times{h} + p = 63cm" />


Onde: 
- \(h\) é a altuda dos espelhos do degrau
- \(p\) é a medida do piso do degrau

## Comece imaginando uma sequência de passos para resolver o problema. Pensar nas perguntas abaixo pode ajudar no processo:
1. Quais são as entradas?
2. Quais são as saídas?
3. Como calcular as saídas a partir das entradas?


______________________________


[Arquivo final](./calculoDeEscadas.py)

______________________________

<!-- language-all: python -->


```Python

import math

# entra do desnivel da escada
desnivel = float(input("entre com o desnível da escada \n"))
# entrada valor máximo para altura de um espelho
espMax = float(input("Digite o espelho máximo \n"))

# número de espelhos
num_esp = desnivel / espMax
# numero de espelhos arredondado
num_esp = math.ceil(num_esp)
# mostrar na tela o número de espelhos
print('número de espelhos', num_esp)

# altura do espelho real
h_esp = desnivel / num_esp
# altura do espelho com 3 casas decimais
h_esp = round(h_esp, 3)

# resultados:
## Número de espelhos
print("o número de espelhos é ", num_esp)
## medida da altura dos espelhos
print("os espelhos tem altura de  ", h_esp)

# calculo do piso pela formula de Blodel
piso = .63 - (2 * h_esp)

## medida do piso
print(" o piso tem ", piso, "m")


```

