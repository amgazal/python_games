import random
l_end=1
h_end=100
ans=random.randint(l_end,h_end)


print('This is a number guessing game. ')
choice=input('Please choose number between '+str(l_end) +' and '+str(h_end)+': ')
play=True
guess=0

while play:
    if choice.isdigit():
        choice=int(choice)
        guess=guess+1
        if int(choice)<int(l_end) or int(choice)>int(h_end):
            print('Please guess from the given range.')
            choice=input('Please choose number between '+str(l_end) +' and '+str(h_end)+': ')


        else:

            if int(choice)<int(ans):
                print('Choose something higher.')
                choice=input('Please choose number between '+str(l_end) +' and '+str(h_end)+': ')

            elif int(choice)>int(ans):
                print('Choose something lower.')
                choice=input('Please choose number between '+str(l_end) +' and '+str(h_end)+': ')

            else:
                print('Great job. You correctly guessed the number which was '+str(ans))
                print('It took you '+str(guess)+ ' guesses to correctly guess.')
                play=False


    else:
        print('Invalid input!')
        print('Please try again')
        choice=input('Please choose number between '+str(l_end) +' and '+str(h_end)+': ')
        guess=guess+1
