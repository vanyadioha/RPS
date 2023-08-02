import random

rock = '👊🏻'
paper = '✋🏻'
scissors = '✌🏻'

game_rules = [rock, paper, scissors]
rule_name = ['Rock', 'Paper', 'Scissors']


def rps_logic():
    player_score = 0
    pc_score = 0
    # Logic
    player_input = input("rock, Paper, Scissors! First to 10pts\nType 0 for Rock, 1 for Paper, 2 for scissors: ")
    player_hand = game_rules[int(player_input)]
    pc_input = random.randint(0, 2)
    pc_hand = game_rules[pc_input]
    if player_hand == rock:
        if pc_hand == paper:
            pc_score += 1
            print('Game Round Lost!')
        elif pc_hand == scissors:
            player_score += 1
            print('Game Round Won!')
        else:
            print('Game Round Drawn!')
    elif player_hand == paper:
        if pc_hand == scissors:
            pc_score += 1
            print('Game Round Lost!')
        elif pc_hand == rock:
            player_score += 1
            print('Game Round Won!')
        else:
            print('Game Round Drawn!')
    else:
        if pc_hand == rock:
            pc_score += 1
            print('Game Round Lost!')
        elif pc_hand == paper:
            player_score += 1
            print('Game Round Won!')
        else:
            print('Game Round Drawn!')
    print(f'You Chose {player_hand}: {rule_name[int(player_input)]}, PC Chose {pc_hand}: {rule_name[pc_input]}')
    print(f'Current Score: Player {player_score} : {pc_score} PC')
    rps_logic()

rps_logic()