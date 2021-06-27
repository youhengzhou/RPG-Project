import random
from engine import engine
import character

hallway = {
    'entry': ['dungeon'],
    'dungeon': ['entry'],
}

def play():
    print('welcome to the dungeon')
    sel = ''
    while(sel != 'q' and 'quit'):
        sel = input('\nenter command: ')

        if sel == 'gen':
            gen()

def gen():
    character.generate()
