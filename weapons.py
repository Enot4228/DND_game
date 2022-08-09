class Weapon:
    def __init__(self, magical='Common'):
        self.abilities = {
            'Common': 0,
            'Rare': 2,
            'Epic': 3,
            'Legendary': 5
        }
        self.rarity = magical
        self.weight = 'light'

    def deal_damage(self):
        import random
        return random.randint(1, 1)


class BattleAxe(Weapon):

    def __init__(self, magical='Common'):
        super(BattleAxe, self).__init__()

        self.rarity = magical
        self.weight = 'heavy'

    def deal_damage(self):
        import random
        return random.randint(1, 8)


class ShortSword(Weapon):

    def __init__(self, magical='Common'):
        super(ShortSword, self).__init__()
        self.rarity = magical
        self.weight = 'medium'

    def deal_damage(self):
        import random
        return random.randint(1, 6) + self.abilities[self.rarity]


class LongBow(Weapon):

    def __init__(self, magical='Common', ammo=20):
        super(LongBow, self).__init__()
        self.ammo = ammo
        self.rarity = magical
        self.weight = 'medium'

    def deal_damage(self):
        import random
        if self.ammo == 0:
            print("You can't shoot, no ammo")
        else:
            self.ammo -= 1
            return random.randint(1, 6)


class Dagger(Weapon):

    def __init__(self, magical='Common'):
        super(Dagger, self).__init__()
        self.rarity = magical
        self.weight = 'light'

    def deal_damage(self):
        import random
        return random.randint(1, 4)


class NoWeapon(Weapon):
    def __init__(self, magical='Common'):
        super(NoWeapon, self).__init__()
        self.rarity = magical
        self.weight = 'None'

    def deal_damage(self):
        import random
        return random.randint(1, 2)


class Staff(Weapon):

    def __init__(self, magical='Common'):
        super(Staff, self).__init__()
        self.rarity = magical
        self.weight = 'medium'

    def deal_damage(self):
        import random
        return random.randint(1, 6)
