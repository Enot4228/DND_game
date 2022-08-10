import random
from time import sleep
import classes
import creatures
import races
import armor
import stash
import weapons
import character


def create_character():
    print('Welcome to DND game in console')
    print('First of all, you need to create a character')
    print('First in creating character is select race of your character')
    while True:
        print('Select your race:')
        print('1. Human\n2. Elf\n3. Dwarf\n4. Halfling')
        races_num = int(input())
        if races_num == 1:
            race_to_char = races.Human()
            break
        elif races_num == 2:
            race_to_char = races.Elf()
            break
        elif races_num == 3:
            race_to_char = races.Dwarf()
            break
        elif races_num == 4:
            race_to_char = races.Halfling()
        else:
            print('You entered wrong number. Try again')
    while True:
        print('Select your class')
        print('1. Warrior\n2. Sorcerer\n3. Priest')
        classes_num = int(input())
        if classes_num == 1:
            classes_to_char = classes.Warrior()
            break
        elif classes_num == 2:
            classes_to_char = classes.Sorcerer()
            break
        elif classes_num == 3:
            classes_to_char = classes.Priest()
            break
        else:
            print('You entered wrong number. Try again')

    while True:
        print('Select your class')
        print('1. Warrior\n2. Sorcerer\n3. Priest')
        classes_num = int(input())
        if classes_num == 1:
            classes_to_char = classes.Warrior()
            break
        elif classes_num == 2:
            classes_to_char = classes.Sorcerer()
            break
        elif classes_num == 3:
            classes_to_char = classes.Priest()
            break
        else:
            print('You entered wrong number')

    while True:
        pass

