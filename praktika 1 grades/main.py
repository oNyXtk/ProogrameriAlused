import sonastik as myDictirionary
import tuples as myTuples

# opilane = {
#     'nimi': "Thomas",
#     'vanus': 20,
#     'klass': "12A"
# }
# print(opilane['nimi'])
# print(opilane.get("vanus"))
# opilane["address"] = "Tallinn"
# opilane.pop('nimi')
# del opilane['klass']
# for key, value in opilane.items():
#     print("see on võti", key, "see on väärtus", value)

# grade = {
#     "mari": [4,5,3,4],
#     "Jaan": [2,3,2,3,3],
#     "Thomas": [3,2,4]
# }
# result = myDictirionary.arvutaKeskmineHinne(grade)
# print(result)
# word = "koodimine"
# result2 = myDictirionary.tahemargede_sagedus(word)
# print(result2)

my_tuple = (2, 4, 5)
print(my_tuple)

tuple2 = ("oun", "pirn", "ploom")  # You can also use parentheses for clarity

andmed_numbers = (10, 15, 20, 25, 30, 35)
tulemus = myTuples.filtreeri_arvud(andmed_numbers)
print(tulemus)

andmed_strings = ["õun", "banaan", "apelsin", "viinamari"]

print(myTuples.leia_indeks(andmed_strings, "apelsin"))
print(myTuples.leia_indeks(andmed_strings, "pirn"))

