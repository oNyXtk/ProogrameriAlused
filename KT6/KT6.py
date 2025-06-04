import random

MIN_RESOURCE_THRESHOLD = 10  # Минимальный порог для "выживания"
RESOURCE_LOSS_PERCENTAGE = 0.2  # 20% теряется при передаче вниз

class Level:
    def __init__(self, level_number, initial_resources):
        self.level_number = level_number
        self.resources = initial_resources
        self.alive = True

    def receive_resources(self, amount):
        if not self.alive:
            return
        self.resources += amount
        print(f"[Уровень {self.level_number}] получил {amount:.1f} ресурсов. Всего: {self.resources:.1f}")

    def transfer_resources(self):
        if not self.alive:
            return 0
        print(f"\nУровень {self.level_number} имеет {self.resources:.1f} ресурсов.")
        print("1. Оставить ресурсы себе")
        print("2. Поделиться (50% себе, 50% передать)")
        print("3. Передать всё на следующий уровень")

        choice = input("Выберите действие (1/2/3): ")

        if choice == '1':
            return 0
        elif choice == '2':
            to_share = self.resources * 0.5
            self.resources *= 0.5
        elif choice == '3':
            to_share = self.resources
            self.resources = 0
        else:
            print("Неверный ввод. Ничего не передано.")
            return 0

        loss = to_share * RESOURCE_LOSS_PERCENTAGE
        transferred = to_share - loss
        print(f"[Уровень {self.level_number}] передаёт {transferred:.1f} ресурсов (потеряно {loss:.1f})")
        return transferred

    def check_survival(self):
        if self.resources < MIN_RESOURCE_THRESHOLD:
            self.alive = False
            print(f"⚠️ Уровень {self.level_number} выбыл! Ресурсов: {self.resources:.1f}")
        return self.alive

class Game:
    def __init__(self, levels=10):
        self.levels = [Level(i + 1, random.randint(20, 50)) for i in range(levels)]

    def play(self):
        print("🎮 Иерархическая игра управления ресурсами началась!\n")
        round_num = 1

        while any(l.alive for l in self.levels):
            print(f"\n🔄 Раунд {round_num}")
            for i in range(len(self.levels)):
                level = self.levels[i]
                if level.alive:
                    transferred = level.transfer_resources()
                    if i + 1 < len(self.levels):
                        self.levels[i + 1].receive_resources(transferred)
                    level.check_survival()
            round_num += 1
            input("\nНажмите Enter для следующего раунда...")

        print("\n💀 Игра окончена. Все уровни выбыли или завершены.")

# Запуск игры
if __name__ == "__main__":
    game = Game(levels=10)
    game.play()
