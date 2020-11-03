import heapq

lista=[]
for i in range (0,10):
    x=input('Descrição da tarefa {}: '.format(i+1))
    y=int(input('Prioridade da tarefa {}: '.format(i+1)))
    heapq.heappush(lista,(y, x))
for i in range (0,10):
    print(heapq.heappop(lista))