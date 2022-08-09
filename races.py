class Race:

    def __init__(self):
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0


class Human(Race):

    def __init__(self):
        super(Human, self).__init__()
        self.strength = 1
        self.dexterity = 1
        self.constitution = 1
        self.intelligence = 1
        self.wisdom = 1
        self.charisma = 1


class Elf(Race):

    def __init__(self):
        super(Elf, self).__init__()
        self.wisdom = 2
        self.intelligence = 2
        self.dexterity = 1


class Dwarf(Race):

    def __init__(self):
        super(Dwarf, self).__init__()
        self.strength = 2
        self.constitution = 2
        self.charisma = 1


class Halfling(Race):

    def __init__(self):
        super(Halfling, self).__init__()
        self.dexterity = 2
        self.constitution = 1
        self.strength = 1
        self.charisma = 1
