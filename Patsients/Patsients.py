class patsient:
    def init(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus
        
class arst:
    def init(self, nimi, vanus, eriala, aeg):
        self.nimi = nimi
        self.vanus = vanus
        self.eriala = eriala  # Исправлено присваивание
        self.aeg = aeg
        
class haigla:
    def init(self):
        self.patsiendilist = []
        self.arstilist = []
        
    def naitaarstid(self):
        for elem in self.arstilist:
            print("arsti nimi: ", elem.nimi, "vanus: ", elem.vanus, "eriala: ", elem.eriala)
            if len(elem.aeg) > 0:
                print("arsti kättesaadav aeg: ")
                for time in elem.aeg:
                    print(time)
                    
    def naitaarst(self, arst):
        for time in arst.aeg:  # Используем объект "arst" и выводим его доступные времена
            print(time)
                    
    def viisitarst(self):
        sisestaarstinimi = input("sisesta arsti nimi: ")
        for elem in self.arstilist:
            if sisestaarstinimi == elem.nimi:
                self.naitaarst(elem)  # Передаем объект "elem" в метод

    def naitapatsient(self):
        for index, elem in enumerate(self.patsiendilist):  # Исправлено использование enumerate
            print("id: ", index, "patsienti nimi: ", elem.nimi, "vanus: ", elem.vanus)
        
# Создание объектов пациентов
pats1 = patsient("anton", 99)
pats2 = patsient("jekaterina", 100)

# Создание объектов врачей
arst1 = arst("muhamad", 8, "kiirurg", ["10:00", "10:30", "11:00", "11:30"])
arst2 = arst("ahmed", 30, "terapeut", ["09:00", "09:30", "10:00", "10:30"])

# Создание объекта больницы
haigla = haigla()

# Добавление врачей в список врачей
haigla.arstilist.append(arst1)
haigla.arstilist.append(arst2)  # Добавлен новый врач Ахмед

# Добавление пациентов в список пациентов
haigla.patsiendilist.append(pats1)
haigla.patsiendilist.append(pats2)

# Вызовы методов
haigla.naitaarstid()  # Показать всех врачей и их доступные времена
haigla.viisitarst()  # Найти врача по имени и показать его доступные времена
haigla.naitapatsient()  # Показать всех пациентов