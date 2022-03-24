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
print(" o piso tem ", round(piso,2), "m")
