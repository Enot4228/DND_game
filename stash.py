class Stash:

    def __init__(self):
        self.cost = 1
        self.quantity = 1


class HealingPotion(Stash):

    def __init__(self):
        super(HealingPotion, self).__init__()
        self.cost = 10
        self.heal = 8
        self.quantity = 3
        self.type = 'Heal'

    def heal(self):
        import random
        return random.randint(1, self.heal)
