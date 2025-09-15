
import random
options=('rock','paper','scissors')
pick=random.choice(options)
print('Ready to play Rock, paper, Scissors?!')
user=input('Please choose (Rock, Paper, Scissors): ').lower()
print('Computer : '+pick)
print('User: '+user)
keep_playing=True


while keep_playing:

    while user not in options:
        print('Please enter a valid input')
        user=input('Please choose (Rock, Paper, Scissors): ').lower()
        print('Computer : '+pick)
        print('User: '+user)

    if user==pick:
        print('Thats a tie!')
        pick=random.choice(options)



    elif user=='scissors' and pick=='paper':
        print('You won !')
        keep_playing=False

    elif user=='paper' and pick=='rock':
        print('You won !')
        keep_playing=False

    elif user=='rock' and pick=='scissors':
        print('You won !')
        keep_playing=False

    else:
        print('You lost!')
        keep_playing=False

    another=input('Would you want to try again(y/n)? ').lower()
    if another=='n':
        print('Thank you for playing!')
        keep_playing=False

    else:
        user=input('Please choose (Rock, Paper, Scissors): ').lower()
        print('Computer : '+pick)
        print('User: '+user)
        keep_playing=True
            
