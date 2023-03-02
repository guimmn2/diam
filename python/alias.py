import time

str1 = "thealiasmen"
str2 = "alan smithee"


def none_approach(word1, word2):
    aux = [*word2.replace(" ", "")]
    print(len(aux))
    print(aux)
    counter = 0
    for char in word1:
        if char != " " and char in word2:
            print(char)
            for i in range(len(aux)):
                if aux[i] == char:
                    aux[i] = "None"
                    counter += 1
    return counter == len(aux)

    


print(none_approach(str1, str2))


