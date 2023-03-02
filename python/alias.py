import itertools
from timeit import default_timer as timer


# função para ordenar
def bubble_sort(l):
    for n in range(len(l)):
        for k in range(len(l) - n - 1):
            if l[k] > l[k + 1]:
                l[k], l[k + 1] = l[k + 1], l[k]
    return l


# strings transponíveis para testar
str1 = "roma"
str2 = "amor"

# Estruturas de controlo

# Alinea a)

print("None Approach:")


def none_approach(word1, word2):
    aux = [*word2.replace(" ", "")]
    counter = 0
    for char in word1:
        if char in aux:
            for i in range(len(aux)):
                if aux[i] == char:
                    aux[i] = "None"
                    counter += 1
                    break
    return counter == len(aux)


start = timer()
flag = none_approach(str1, str2)
end = timer()

print("Strings são transponíveis: " + str(flag) + " - none approach utilizou 2 passos e demorou: " + str(end - start))
print(". . .")


# Alinea b)
def sort_approach(word1, word2):
    aux1 = bubble_sort([*word1.replace(" ", "")])
    aux2 = bubble_sort([*word2.replace(" ", "")])
    return aux1 == aux2


start = timer()
flag = sort_approach(str1, str2)
end = timer()

print("Sort Approach:")
print("Strings são transponíveis: " + str(
    flag) + " - sort approach utilizou 4 passos (2 em cada sort) e demorou: " + str(end - start))
print(". . .")


# Alinea c)
def brute_force_approach(word1, word2):
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    return word2 in [''.join(p) for p in itertools.permutations(word1)]


start = timer()
flag = brute_force_approach(str1, str2)
end = timer()
print("Brute force Approach:")
print(
    "Strings são transponíveis: " + str(
        flag) + " - brute force approach utilizou 4 passos (neste caso pois o length das strings é 4) e demorou: " + str(
        end - start))
print(". . .")


# Alinea d)
def word_count_approach(word1, word2):
    word1 = word1.replace(" ", "")
    word2 = word2.replace(" ", "")
    w1 = {}
    w2 = {}
    for c in word1:
        if w1.get(c) is not None:
            w1[c] += 1
        else:
            w1[c] = 1
    for c in word2:
        if w2.get(c) is not None:
            w2[c] += 1
        else:
            w2[c] = 1

    for k in w1.keys():
        if w2.get(k) is None:
            return False
        if w2.get(k) != w1.get(k):
            return False
    return True


start = timer()
flag = word_count_approach(str1, str2)
end = timer()
print("Word Count Approach: ")
print("Strings são transponíveis: " + str(flag) + " - word count approach utilizou 3 passos e demorou: " + str(
    end - start))
print(". . .")

#Alínea e)

#A que tem menos passos é a alinea a) none approach. Se forem usadas strings muito pequenas (<4 letras) o brute force acaba por ser o mais rapido,
# mas para as maiores strings o none approach é o mais rapido

