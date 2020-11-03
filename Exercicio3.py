matriz=[]
for i in range (0,10):
    linha=[]

    for i in range (0,10):
        linha.append(int(input('Digite sua matriz: ')))
    matriz.append(linha)

for i in range (0,10):
    print (matriz[i])