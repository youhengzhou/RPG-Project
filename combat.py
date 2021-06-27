import random
from engine import engine
import character
import operator

attack_types=['strength','endurance','dexterity']

def stat(char):
    print('stat here')
    print(char)

def train(player_char):
    print('train here')
    r1 = random.randint(0, len(attack_types)-1)
    r2 = random.randint(-1, 2)
    player_char[attack_types[r1]] = player_char[attack_types[r1]] + r2
    print(player_char['name'] + ' tweaked ' + attack_types[r1] + ' by ' + str(r2))
    return player_char

def heal(player_char):
    player_char['health']=player_char['health']+1
    player_char['money']=player_char['money']-1
    return player_char

def wait():
    enemy_char=character.character_init()
    return enemy_char

def combat(player_char, enemy_char):
    winner = -1
    turn = 1

    player_attacks=[]
    enemy_attacks=[]

    player_attacks.append(player_char['strength'])
    player_attacks.append(player_char['endurance'])
    player_attacks.append(player_char['dexterity'])

    enemy_attacks.append(enemy_char['strength'])
    enemy_attacks.append(enemy_char['endurance'])
    enemy_attacks.append(enemy_char['dexterity'])

    player_highest_attack_index, player_highest_attack_value = max(enumerate(player_attacks), key=operator.itemgetter(1))
    enemy_highest_attack_index, enemy_highest_attack_value = max(enumerate(enemy_attacks), key=operator.itemgetter(1))

    if player_char['dexterity'] > enemy_char['dexterity']:
        turn = 1
        print('the player went first with ' + str(player_char['dexterity']) + ' over ' + str(enemy_char['dexterity']))
    else:
        turn = 2
        print('the enemy went first with ' + str(enemy_char['dexterity']) + ' over ' + str(player_char['dexterity']))

    while(winner == -1):
        if turn % 2 == 1:
            enemy_char['health']=enemy_char['health']-player_attacks[player_highest_attack_index]
            print(player_char['name'] + ' used his ' + str(attack_types[player_highest_attack_index]) + ' to deal ' + str(player_highest_attack_value) + ' damage')
        else:
            player_char['health']=player_char['health']-enemy_attacks[enemy_highest_attack_index]
            print(enemy_char['name'] + ' used his ' + str(attack_types[enemy_highest_attack_index]) + ' to deal ' + str(enemy_highest_attack_value) + ' damage')
        if(player_char['health'] <= 0):
            winner = 0
            print('the player lost')
        elif(enemy_char['health'] <= 0):
            winner = 1
            player_char['money'] = player_char['money'] + enemy_char['money']
            print('the player won and gained ' + str(enemy_char['money']) + ' money')
        turn = turn + 1
