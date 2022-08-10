import random


class Character:

    def __init__(self, name, race, classes, stash, armor, weapon):
        self.name = name
        self.race = race
        self.classes = classes
        self.stash = stash
        self.armor = armor
        self.weapon = weapon
        self.dead = 0

    def death(self):
        self.dead = 1

    def take_damage(self, damage):
        self.classes.hp -= damage

    def deal_damage(self):
        return self.weapon.deal_damage() + self.race.strength

    def short_rest(self, number_of_heal_dices):
        for i in range(0, number_of_heal_dices):
            self.classes.hp += random.randint(1, self.classes.heal_dice)
        self.classes.heal_dice_count -= number_of_heal_dices

    def long_rest(self):
        self.classes.hp = self.classes.max_hp

