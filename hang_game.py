
#Guess-the-word Game
from wordyl import words
import random

hangman_art = {0: ("   ",
                    "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}

def display_man(wrong_guess):
    print('************')
    for line in hangman_art[wrong_guess]:
        print(line)
    print('*************')


def display_hint(hint):
    print(' '.join(hint))

def display_ans(answer):
    print(' '.join(answer))

def main():
    print('How vast is your vocabulary\nHow good is your guessing game\nLet''s see for ourselves, shall we?')
    answer=random.choice(words)
    hint=['_']*len(answer)
    wrong_guess=0
    is_playing=True
    guessed_ans=set()

    while is_playing:
        display_man(wrong_guess)
        display_hint(hint)
        print()
        user=input('Guess a letter: ').strip().lower()
        if len(user)!=1:
            print('Make sure you are guessing a single letter at a time')
            continue

        if not user.isalpha():
            print('Invalid input\nWords not numbers')
            continue

        if user in guessed_ans:
            print('You already guessed this letter')
            continue

        guessed_ans.add(user)

        if user in answer:
            for index in range(len(answer)):
                if answer[index]==user:
                    hint[index]=user


        else:
            wrong_guess+=1

        if not '_' in hint:
            display_man(wrong_guess)
            display_hint(hint)
            display_ans(answer)
            print('Bravo: you won !!!')
            print('It took you '+str(wrong_guess)+' number of guesses to win.')
            print()
            print()
            print()
            to_play_again=input('To play again, please press y(pressing any other key will lead to you quitting): ').strip().lower()
            if to_play_again=='y':
                answer=random.choice(words)
                hint=['_']*len(answer)
                wrong_guess=0
                guessed_ans=set()
                print('\n<<<New Round>>>\n')

            else:
                is_playing=False


        elif wrong_guess>=len(hangman_art)-1:
                display_man(wrong_guess)
                display_hint(hint)
                print('Sorry you lost\nThe correct word was '+answer)
                print('Better luck next time')

                to_play_again=input('To play again, please press y(pressing any other key will lead to you quitting): ').strip().lower()
                if to_play_again=='y':
                    is_playing=True
                    answer=random.choice(words)
                    hint=['_']*len(answer)
                    wrong_guess=0
                    guessed_ans=set()
                    print('\n<<<New Round>>>\n')
                else:
                    is_playing=False







if __name__=='__main__':
    main()
