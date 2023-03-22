poem = """Eu hoje fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo"""

# 3.1 Strings

# Alinea a)

verse_list = poem.split(" / ")

print("verse 5: " + verse_list[4])
print("verse 6: " + verse_list[5])
print(". . .")

# Alinea b)

parsed_poem = poem.replace(" / ", "\n")

print("Poema formatado:")
print(parsed_poem)
print(". . .")

# Alinea c)

print("adicionando a estrofe...")

verse_list.append("Por isso eu fiz um samba bem pra frente")
verse_list.append("Dizendo realmente o que é que eu acho")
verse_list.append("Isso me deixa triste e cabisbaixo")
for verse in verse_list:
    print(verse)
print(". . .")

# Alinea d)

# print dos ultimos 2 versos adicionados
print("Últimos dois versos: ")
for verse in verse_list[-2:]:
    print(verse)
