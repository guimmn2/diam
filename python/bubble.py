import random
import time

l_length = 100
l = []
for i in range(l_length):
    l.append(random.randint(1, 99))

print("lista aleatória: " + str(l))

#bubble_sort
print("começando algoritmo de ordenação")

start = time.time()

while l != sorted(l):
    for n in range(len(l) - 1):
        if l[n] > l[n+1]:
            l[n], l[n+1] = l[n+1], l[n]

end = time.time()

print("list ordenada: " + str(l)) 

print("tempo de execução: " + str(end - start))
