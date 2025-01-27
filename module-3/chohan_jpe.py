# Author: Julio Pochet Edmead
# Assignment: Module 3.2 - Brownfield Development
# Purpose: Modified the Cho-Han game as per assignment requirements.
#
# Changes made:
# 1. Changed the input prompt to use my initials and a colon 'JP:' instead of default input prompt.
# 2. Increased the house fee from 10% to 12%.
# 3. Added a notice in the introduction about the 10 mon bonus for rolling 2 or 7.
# 4. Implemented a check to grant a 10 mon bonus when the total dice roll is 2 or 7.
# 5. Adjusted the house fee calculation to correctly deduct 12%.

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

NOTICE: If the total dice roll is 2 or 7, you receive a 10 mon bonus!
''')

purse = 5000
while True:  # Main game loop.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('JP: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('JP: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    total_roll = dice1 + dice2
    if total_roll == 2 or total_roll == 7:
        print(f'JP: Congratulations! You rolled a {total_roll} and receive a 10 mon bonus.')
        purse += 10

    if playerWon:
        print('You won! You take', pot, 'mon.')
        house_fee = int(pot * 0.12)  # 12% house fee
        purse = purse + pot - house_fee
        print('The house collects a', house_fee, 'mon fee.')
    else:
        purse = purse - pot
        print('You lost!')

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
