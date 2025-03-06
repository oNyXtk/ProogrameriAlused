def filtreeri_arvud(andmed):
    tulem = []
    for num in andmed:
        if num % 10 == 0:
            tulem.append(num)
    return tulem

def leia_indeks(nimekiri, element):
    if element in nimekiri:
        return nimekiri.index(element)
    else:
        return -1
