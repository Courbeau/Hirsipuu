import random

uusisana = ""

lista = [("k", "i", "s", "s", "a"), ("j", "a", "l", "k", "a", "p", "a", "l", "l", "o"), "asunto"]
hidword = ""

a = random.randint(0, 2)

sana = lista[a]

for i in sana:
    hidword = hidword + "_"

print("Vihje: " + hidword)

sanavaikirjain = input("Haluatko arvata sanaa vai kirjainta? 0 jos sanaa, 1 jos kirjainta: ")

if sanavaikirjain == "0":
    sana_arvaus = input("Arvaa sanaa: ")

    #tää kohta

if sanavaikirjain == "1":
    kirjain_arvaus = input("Arvaa kirjainta: ")
    if kirjain_arvaus in lista[0]:
        for kirjain in lista[0]:
            if kirjain_arvaus == kirjain:
                uusisana = uusisana + kirjain
            else:
                uusisana = uusisana + "_"
    else:
        print("Ei ole")


print(uusisana)


