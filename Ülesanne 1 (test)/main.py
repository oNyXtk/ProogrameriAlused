#Ülesanne 1 Kalkulattor. lahutame hinnast allahindluse protsendi ja jagame selle 100-ga#

hind = float(input("Kauba hind: "))
soodustus = float(input("Soodustus: "))
lõplik_hind = hind - (hind * soodustus / 100)
print(f"Lõplik hind: {lõplik_hind}")

#Ülesanne 2 eksami hinne. Kasutame käsku input täisarvu saamiseks ja selle teisendamiseks int. if, elif, else kasutatakse selleks, et kontrollida vahemikku, kuhu sisestatud arv jääb, ja väljastab vastava hinnangu

tulemus = int(input("Sisesta eksami tulemus protsentides: "))
if 0 <= tulemus <= 100:
    if tulemus < 50:
        print("Hinne: 2 (Mitte sooritatud)")
    elif 50 <= tulemus <= 74:
        print("Hinne: 3 (Rahuldav)")
    elif 75 <= tulemus <= 89:
        print("Hinne: 4 (Hea)")
    else:
        print("Hinne: 5 (Väga hea)")
else:
    print("Viga: Sisestage arv vahemikus 0–100.")

#Ülesanne 3 Korutustable. andmete sisestamiseks. Vormingutring aitab meil arve nende sisestamisel korrutada. see on loendur tsüklis 1 kuni 10. ja see väljastab korrutamise tulemuse

arv = int(input("Sisesta arv: "))
for i in range(1, 11):
    print(f"{arv} x {i} = {arv * i}")


#Ülesanne 4. Arva ära number. kasutame käsku IMPORT RANDOM. RANDOM RANDIT 1-10, nii et tsükkel arvab ära juhusliku arvu vahemikus 1 kuni 10. Numbri äraarvamisel kasutame tsükli peatamiseks käsku BREAK, vastasel juhul jätkame.

    import random

# Valib juhusliku arvu vahemikus 1 kuni 10
salajane_number = random.randint(1, 10)

# Küsi kasutajalt arvu äraarvamise katset
while True:
    arvamus = int(input("Arva ära number (1-10): "))
    if arvamus == salajane_number:
        print("Õige!")
        break
    else:
        print("Proovi uuesti!")

#Ülesanne 5 Lihtne Kalkulattor. Kalkulaator töötab nii, et näeb, mis sümboliga inimene sõidab ja numbreid tänu käsklustele. See loeb ülesande sümbolid ja kui korrutis on 0 sümbolit, annab veateate, et arvu ei korrutata 0-ga

esimene_arv = float(input("Sisesta esimene arv: "))
teine_arv = float(input("Sisesta teine arv: "))
operaator = input("Sisesta operaator (+, -, *, /): ")

if operaator == "+":
    tulemus = esimene_arv + teine_arv
elif operaator == "-":
    tulemus = esimene_arv - teine_arv
elif operaator == "*":
    tulemus = esimene_arv * teine_arv
elif operaator == "/":*
    if teine_arv != 0:
        tulemus = esimene_arv / teine_arv
    else:
        tulemus = "Jagamine nulliga ei ole lubatud!"
else:
    tulemus = "Viga: Ebalevine operaator."

print(f"Tulemus: {tulemus}")



