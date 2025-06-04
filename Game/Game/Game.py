class Level:
    def __init__(self):
        self.resource_amount = 50  
        self.world_resources = 2000  


class Player:
    def __init__(self):
        self.inventory_size = 8
        self.health_capacity = 100
        self.stamina_capacity = 100
        self.damage_output = 50
        self.critdamage_output = 75

    def crit_damage(self, crit):
        if crit:
            print(self.critdamage_output)
        else:
            print(self.damage_output)


class World:
    def __init__(self):
        self.world_time = "10:00"
        self.total_resources = 2000
        self.trees = 30


class Resources:
    def __init__(self):
        self.apple = 500
        self.bread = 500
        self.milk = 500
        self.gold = 500

    def food_reserve(self):
        print(f"Food reserve: Apple: {self.apple}, Bread: {self.bread}, Milk: {self.milk}, Gold: {self.gold}")


class Platform:
    def __init__(self):
        self.resource_reserve = 70
        self.food_reserve = 20

    def transfer_resources(self, player):
        print(f"Transferring resources to player,  Food reserve: {self.food_reserve}")


class LevelingSystem:
    def __init__(self):
        self.xp_requirement = 500
        self.advance_to_the_new_level = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def level_up(self, current_xp, player_level):
        if current_xp >= self.xp_requirement:
            self.xp_requirement *= 2  
            player_level += 1
            print(f"Player has advanced to the new level {player_level}")
        else:
            print(f"XP requirement: {self.xp_requirement}")


class Monsters:
    def __init__(self):
        self.BJ_health_capacity = 100
        self.BJ_damage_output = 75
        self.BJ_immunity = True  
        self.Benji_health_capacity = 70
        self.Benji_damage_output = 85
        self.Benji_fire_resistance = True  
    def attack(self):
        print("Monsters has seen you and start attacking !")


class Bosses:
    def __init__(self):
        self.boss_name = "JJ"
        self.boss_health = 1000
        self.boss_damage = 200
    def boss_attack(self):
        print(f"{self.boss_name} is attacking with {self.boss_damage} damage")
        
class Player1:
    def __init__(self):
        self.Ryu_health = 100
        self.Ryu_damage = 60
        self.Ryu_stamina = 70
    def Player1_attack(self):
        print(f"Ryu is attacking JJ with {self.Ryu_damage} damage")
        
    



player1 = Player1()
player = Player()
level = Level()
world = World()
resources = Resources()
platform = Platform()
leveling_system = LevelingSystem()
monsters = Monsters()
bosses = Bosses()
player.crit_damage(crit=True)
platform.transfer_resources(player)
leveling_system.level_up(600, 1)
monsters.attack()
bosses.boss_attack()

         
    

    
    
    
    
        
    