import time
from itertools import permutations

str1 = "r   oma"
str2 = "amo r"


#O(n²)
def none_approach(word1, word2):
    aux = [*word2.replace(" ", "")]
    counter = 0
    for char in word1:
        if char != " " and char in word2:
            for i in range(len(aux)):
                if aux[i] == char:
                    aux[i] = "None"
                    counter += 1
    return counter == len(aux)

    


print(str(none_approach(str1, str2)))

#O(2n*logn)
#Provavelmente teremos que refazer este... À espera da resposta do prof
def sort_approach(word1, word2):
    aux1 = sorted([*word1.replace(" ", "")])
    aux2 = sorted([*word2.replace(" ", "")])
    return aux1 == aux2

print(sort_approach(str1, str2))


#Provavelmente teremos que refazer este... À espera da resposta do prof
def brute_force_approach(word1, word2):
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    return word2 in [''.join(p) for p in permutations(word1)]

print(brute_force_approach(str1, str2))

#3 passos (no pior cenário)
def word_count_approach(word1, word2):
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    w1 = {}
    w2 = {}
    for c in word1:
        if w1.get(c) != None:
            w1[c] += 1
        else:
            w1[c] = 1
    for c in word2:
        if w2.get(c) != None:
            w2[c] += 1
        else:
            w2[c] = 1

    for k in w1.keys():
        if w2.get(k) == None:
            return False
        if w2.get(k) != w1.get(k):
            return False
    return True

print(word_count_approach(str1, str2))
