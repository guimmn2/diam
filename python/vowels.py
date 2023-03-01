#3.2
poem = """Eu hoje fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo"""

verse_list = poem.split(" / ")

parsed_poem = poem.replace(" / ", "\n")

vowel_count = 0
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for char in parsed_poem:
    if char in ['a','e','i','o','u']:
        vowel_count += 1
        if char == 'a':
            a_count += 1
        elif char == 'e':
            e_count += 1
        elif char == 'i':
            i_count += 1
        elif char == 'o':
            o_count += 1
        else:
            u_count += 1

"""
print("contagem de vogais:")
print("...")
print("a: " + str(a_count) + "\n" +"e: " + str(e_count) + "\n" +"i: " + str(i_count) + "\n" +"o: " + str(o_count) + "\n" +"u: " + str(u_count))
print("...")

vowel_counts = sorted([a_count, e_count, i_count, o_count, u_count])

if vowel_counts[-1] == vowel_counts[-2]:
    print("Há mais vencedores")
else:
    print("vogal vencedora: " + str(vowel_counts[-1]))
"""



