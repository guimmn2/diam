import time

str1 = "the alias men"
str2 = "alan smithee"


#O(n²)
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

    


print(str(none_approach(str1, str2)))

#O(2n*logn)
def sort_approach(word1, word2):
    aux1 = sorted([*word1.replace(" ", "")])
    aux2 = sorted([*word2.replace(" ", "")])
    return aux1 == aux2

print(sort_approach(str1, str2))




