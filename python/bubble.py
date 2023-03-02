import random
import time

l_length = 100
l = []
for i in range(l_length):
    l.append(random.randint(1, 99))
l2 = l.copy()

print("lista aleatória: " + str(l))
print(". . .")


#bubble_sort podre
print("começando com algoritmo de ordenação")
print(". . .")

start_1 = time.time()

for n in range(len(l)):
    for k in range(len(l) - 1):
        if l[k] > l[k+1]:
            aux = l[k]
            l[k] = l[k+1]
            l[k+1] = aux

end_1 = time.time()

print("list ordenada: " + str(l)) 
print(". . .")

#bubble_sort
print("começando algoritmo de ordenação optimizado")
print(". . .")

start_2 = time.time()

for n in range(len(l2)):
    for k in range(len(l2) - n - 1):
        if l2[k] > l2[k+1]:
            l2[k], l2[k+1] = l2[k+1], l2[k]

end_2 = time.time()

print("list ordenada: " + str(l2)) 
print(". . .")

print("tempo de execução para o 1º algoritmo: " + str(end_1 - start_1))
print("tempo de execução para o 2º algoritmo: " + str(end_2 - start_2))
