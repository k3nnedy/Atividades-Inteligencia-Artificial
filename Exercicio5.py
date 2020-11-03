from collections import deque #Usando a biblioteca Deque pa

fila=deque([]) # Cria uma fila

for i in range (0,10): # Adiciona os elementos
    fila.append(int(input('Digite um numero: ')))

for i in range(0,10): #Printa os elementos da fila (remove)
    fila(fila.popleft())