# 3.2
poem = """Eu hoje fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo"""

verse_list = poem.split(" / ")

parsed_poem = poem.replace(" / ", "\n")

vowels_dict = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for char in parsed_poem:
    if char in vowels_dict.keys():
        vowels_dict[char] += 1

print("...")
print("Ocorrências de cada vogal:")
print(vowels_dict)
print("...")

# vogal mais utilizada/vogais empatadas
max_value = max(vowels_dict.values())
tied_vowels = []
for pair in vowels_dict.items():
    if pair[1] == max_value:
        tied_vowels.append(pair[0])
if len(tied_vowels) > 1:
    print("há mais vencedoras: " + str(tied_vowels))
else:
    print("vencedora: " + str(tied_vowels))


