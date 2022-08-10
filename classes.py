import random
class Classes:

    def __init__(self):
        self.armor = None
        self.weapon = None
        self.stash = None
        self.level = 1


class Warrior(Classes):

    def __init__(self):
        super(Warrior, self).__init__()
        self.armor = ['heavy', 'medium', 'light']
        self.weapon = ['heavy', 'medium', 'light']
        self.stash = ['Heal']
        self.level = 1
        self.heal_dice = 10
        self.heal_dice_count = 1
        self.hp = random.randint(1, 10)
        self.max_hp = self.hp  # Могут быть баги
        self.power_strike_damage = 6

    def power_strike(self):
        return random.randint(1, self.power_strike_damage)


class Sorcerer(Classes):

    def __init__(self):
        super(Sorcerer, self).__init__()
        self.armor = ['light']
        self.weapon = ['light', 'medium']
        self.stash = ['Heal']
        self.level = 1
        self.heal_dice = 8
        self.heal_dice_count = 1
        self.hp = random.randint(1, 8)
        self.max_hp = self.hp  # Могут быть баги
        self.fire_bolt_damage = 8

    def fire_bolt(self):
        return random.randint(1, self.fire_bolt_damage)


class Priest(Classes):

    def __init__(self):
        super(Priest, self).__init__()
        self.armor = ['light']
        self.weapon = ['light']
        self.stash = ['Heal']
        self.level = 1
        self.hp = random.randint(1, 8)
        self.max_hp = self.hp # Могут быть баги
        self.heal_dice = 8
        self.heal_dice_count = 1
        self.smite_damage = 4
        self.small_heal_healing = 6

    def smite(self):
        return random.randint(1, self.smite_damage)

    def small_healing(self, target):
        target.hp += random.randint(1, self.small_heal_healing)
