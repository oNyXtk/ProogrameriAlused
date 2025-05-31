import random

class Player:
    def __init__(self):
        self.name = "Cloud"
        self.health = 100
        self.damage = 20
        self.gold = 100
        self.xp = 0
        self.level = 1
        self.weapon_level = 1
        self.defending = False
        self.inventory = []

    def attack(self):
        return self.damage

    def add_item(self, item):
        self.inventory.append(item)
        print(f"🧾 {item['name']} added to inventory.")

    def use_item(self):
        if not self.inventory:
            print("Inventory is empty.")
            return False

        print("\n🧪 Choose an item to use:")
        for i, item in enumerate(self.inventory, 1):
            print(f"{i}. {item['name']}")

        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(self.inventory):
                item = self.inventory.pop(choice)
                if item["type"] == "healing":
                    healed = min(item["value"], 100 - self.health)
                    self.health += healed
                    print(f"❤️ {self.name} healed for {healed} HP! (Now at {self.health})")
                    return True
                else:
                    print("Nothing happened...")
            else:
                print("Invalid selection.")
        except:
            print("Invalid input.")
        return False

    def take_damage(self, amount):
        if self.defending:
            amount //= 2
            print(f"{self.name} defends and takes only {amount} damage!")
            self.defending = False
        self.health -= amount

    def level_up(self):
        if self.xp >= 100:
            self.level += 1
            self.health = 100
            self.damage += 5
            self.xp = 0
            print(f"{self.name} leveled up! Now level {self.level} with {self.damage} damage.")

class Enemy:
    def __init__(self, name, health, damage, reward_gold, reward_xp, drop_item=None):
        self.name = name
        self.health = health
        self.damage = damage
        self.reward_gold = reward_gold
        self.reward_xp = reward_xp
        self.drop_item = drop_item

class Blacksmith:
    def __init__(self):
        self.upgrade_cost = 50

    def upgrade_weapon(self, player):
        if player.gold >= self.upgrade_cost:
            player.gold -= self.upgrade_cost
            player.damage += 10
            player.weapon_level += 1
            self.upgrade_cost += 30
            print(f"🔨 Weapon upgraded to level {player.weapon_level}! Damage now {player.damage}")
        else:
            print("Not enough gold to upgrade.")

class Shop:
    def __init__(self):
        self.items_for_sale = [
            {"name": "Healing Potion", "type": "healing", "value": 30, "price": 20},
            {"name": "Mega Potion", "type": "healing", "value": 60, "price": 40}
        ]

    def visit_shop(self, player):
        print("\n🛒 Welcome to the Item Shop!")
        for i, item in enumerate(self.items_for_sale, 1):
            print(f"{i}. {item['name']} - {item['price']} gold (Heals {item['value']} HP)")

        print(f"\n💰 Your gold: {player.gold}")
        print("Choose an item to buy or 0 to cancel:")

        try:
            choice = int(input("> "))
            if choice == 0:
                return
            if 1 <= choice <= len(self.items_for_sale):
                item = self.items_for_sale[choice - 1]
                if player.gold >= item["price"]:
                    player.gold -= item["price"]
                    player.add_item(item)
                    print(f"✅ Bought {item['name']} for {item['price']} gold.")
                else:
                    print("❌ Not enough gold.")
            else:
                print("❗ Invalid choice.")
        except:
            print("❗ Invalid input.")

def battle(player, enemy):
    print(f"\n⚔️ A wild {enemy.name} appears!")
    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name} HP: {player.health} | {enemy.name} HP: {enemy.health}")
        print("Choose action: (1) Attack (2) Defend (3) Use Item")
        choice = input("> ")

        if choice == "1":
            dmg = player.attack()
            enemy.health -= dmg
            print(f"{player.name} attacks for {dmg} damage!")
        elif choice == "2":
            player.defending = True
            print(f"{player.name} is defending!")
        elif choice == "3":
            used = player.use_item()
            if not used:
                print("Turn wasted...")
        else:
            print("Invalid choice. Turn wasted.")

        if enemy.health > 0:
            player.take_damage(enemy.damage)
            print(f"{enemy.name} attacks for {enemy.damage} damage!")

    if player.health > 0:
        print(f"\n✅ You defeated {enemy.name}!")
        player.gold += enemy.reward_gold
        player.xp += enemy.reward_xp
        print(f"💰 Gained {enemy.reward_gold} gold and {enemy.reward_xp} XP!")
        if enemy.drop_item:
            player.add_item(enemy.drop_item)
        player.level_up()
    else:
        print("\n❌ You were defeated...")

def main_game():
    player = Player()
    blacksmith = Blacksmith()
    shop = Shop()

    enemies = [
        Enemy("Slime", 60, 15, 30, 50, {"name": "Healing Potion", "type": "healing", "value": 30}),
        Enemy("Goblin", 80, 20, 40, 60, {"name": "Mega Potion", "type": "healing", "value": 60}),
        Enemy("Skeleton", 100, 25, 50, 70, {"name": "Healing Potion", "type": "healing", "value": 40})
    ]

    boss1 = Enemy("Dark Knight", 200, 40, 100, 150, {"name": "Mega Potion", "type": "healing", "value": 80})
    boss2 = Enemy("Dragon Lord", 300, 60, 200, 300, {"name": "Legendary Elixir", "type": "healing", "value": 100})

    while True:
        print("\nMain Menu:")
        print("1. Fight enemy")
        print("2. Visit blacksmith")
        print("3. Show stats")
        print("4. Show inventory")
        print("5. Visit shop")
        print("6. Fight boss")
        print("7. Exit game")
        choice = input("> ")

        if choice == "1":
            enemy = random.choice(enemies)
            battle(player, enemy)
            player.health = 100
        elif choice == "2":
            blacksmith.upgrade_weapon(player)
        elif choice == "3":
            print(f"\n📊 {player.name} - Level {player.level}")
            print(f"Health: {player.health}")
            print(f"Damage: {player.damage}")
            print(f"Gold: {player.gold}")
            print(f"XP: {player.xp}")
        elif choice == "4":
            print("\n🎒 Inventory:")
            if player.inventory:
                for i, item in enumerate(player.inventory, 1):
                    print(f"{i}. {item['name']}")
            else:
                print("Inventory is empty.")
        elif choice == "5":
            shop.visit_shop(player)
        elif choice == "6":
            if player.level < 3:
                print("❗ You must be at least level 3 to challenge a boss.")
            else:
                print("Choose your boss: (1) Dark Knight (2) Dragon Lord")
                b_choice = input("> ")
                if b_choice == "1":
                    battle(player, boss1)
                elif b_choice == "2":
                    battle(player, boss2)
                else:
                    print("Invalid boss selection.")
        elif choice == "7":
            print("👋 Goodbye, hero!")
            break
        else:
            print("❗ Invalid input.")

main_game()

    
        
    