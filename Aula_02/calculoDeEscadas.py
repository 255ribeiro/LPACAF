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
