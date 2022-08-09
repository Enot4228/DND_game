import random


class Creature:

    def __init__(self):
        self.hp = 1
        self.damage = 0
        self.armor = 5
        self.dead = 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.death()

    def death(self):
        self.dead = 1


class Living(Creature):

    def __init__(self):
        super(Living, self).__init__()
        self.damage = 1

    def deal_damage(self):
        return random.randint(1, self.damage)


class Monster(Creature):

    def __init__(self):
        super(Monster, self).__init__()
        self.hp = 6
        self.armor_class = 12
        self.damage = 4

    def deal_damage(self):
        return random.randint(1, self.damage)


class Wolf(Monster):

    def __init__(self):
        super(Wolf, self).__init__()


class Orc(Monster):

    def __init__(self):
        super(Orc, self).__init__()
        self.hp = 9
        self.armor_class = 14
        self.damage = 6


class Ogre(Monster):

    def __init__(self):
        super(Ogre, self).__init__()
        self.hp = 14
        self.armor_class = 13
        self.damage = 8
