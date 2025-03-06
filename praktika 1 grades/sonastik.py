def arvutaKeskmineHinne(grades):
    averageGrades = {}
    for name, grades in grades.items():
        averageGrades[name] = sum(grades)/len(grades)
    return averageGrades

def tahemargede_sagedus(word):
    sagedus = {}
    for symbol in word:
        sagedus[symbol] = sagedus.get(symbol, 0) + 1
    return sagedus
