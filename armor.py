class Armor:

    def __init__(self):
        self.weight = 'medium'
        self.armor_class = 10


class LightArmor(Armor):

    def __init__(self):
        super(LightArmor, self).__init__()
        self.weight = 'light'
        self.armor_class = 12


class MediumArmor(Armor):

    def __init__(self):
        super(MediumArmor, self).__init__()
        self.weight = 'medium'
        self.armor_class = 14


class HeavyArmor(Armor):

    def __init__(self):
        super(HeavyArmor, self).__init__()
        self.weight = 'heavy'
        self.armor_class = 17
