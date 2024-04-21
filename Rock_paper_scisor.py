import random

play='yes'
while play=='yes':
    choice=['rock','paper','scissor']

    computer=random.choice(choice)
    player=None
    while player not in choice:
        player=input("rock, paper or scissor ?\n").lower()

    if player==computer:
        print("Its a tie")
        print('Computer : ',computer)
        print('Player : ',player)
    else:
        if player=='rock':
            if computer=='scissor':
                print('Woohow! You won :)')
            else:
                print('Sorry! You lose :(')
            print('Computer : ',computer)
            print('Player : ',player)

        if player=='paper':
            if computer=='rock':
                print('Woohow! You won :)')
            else:
                print('Sorry! You lose :(')
            print('Computer : ',computer)
            print('Player : ',player)

        if player=='scissor':
            if computer=='paper':
                print('Woohow! You won :)')
            else:
                print('Sorry! You lose :(')
            print('Computer : ',computer)
            print('Player : ',player)
    play=None
    while play!='yes' and play!='no':
        play=input('Do you want to play again Yes/No ?').lower()





