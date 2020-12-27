import random

lista = [("k", "i", "s", "s", "a"), "jalkapallo", "asunto"]
hidword = ""

a = random.randint(0, 2)

sana = lista[a]

for i in sana:
    hidword = hidword + "_"

print("Vihje: " + hidword)

sanavaikirjain = input("Haluatko arvata sanaa vai kirjainta? 0 jos sanaa, 1 jos kirjainta: ")

if sanavaikirjain == "0":
    sana_arvaus = input("Arvaa sanaa: ")
    if sana_arvaus == sana:
        print("Oikein meni, voitit!")
    else:
        print("Väärin meni")

if sanavaikirjain == "1":
    kirjain_arvaus = input("Arvaa kirjainta: ")

    if sana.find(kirjain_arvaus) > -1:
        hidword
        
        
uusisana = ""

if kirjain_arvaus in lista[0]:
    for kirjain in lista[0]:
        if kirjain_arvaus == kirjain:
            uusisana = uusisana + kirjain
        else:
            uusisana = uusisana + "_"
else:
    print("Ei ole")

