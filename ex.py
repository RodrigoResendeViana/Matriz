matriz = []

for i in range(3):
    linha = []
    for j in range(5):
        n = int(input('Digite um número: '))
        linha.append(n)
    matriz.append(linha)

print(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    print()

