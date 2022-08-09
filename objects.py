class Character:

    def __init__(self, name, race, clas, armor, stash, weapon):
        self.name = name
        self.armor = armor
        self.race = race
        self.stash = stash
        self.weapon = weapon
        self.clas = clas

    def healing(self, what_use):
        if what_use == 1:
            pass
        else:
            pass

    def deal_damage(self):
        pass

    def take_damage(self):
        pass

    def death(self):
        pass

