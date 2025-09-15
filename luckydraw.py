# python
name=input('Hello, what is your name? ')
age=int(input('How old are you? '))
if age>=18:
    consent=input('Do you agree to the terms and conditions required to play this game? '+name+' (Y/N)')
    while consent =='N' or consent=='no':
        consent=input('We cannot proceed without your consent, '+name+'. Please type in a capital Y for consent or a capital N for no. Do you agree to the T&Cs: ')

    ready= input('Are you ready to proceed? (Y/N)')
    if ready=='Y':
        draw= int(input(' Please pick a number within the range, '+name+': '))
        while draw>100 or draw<1:
            draw=int(input('You need to draw a number between 1 and a 100. Kindly tru again: '))
        while draw<55 or draw>65:
            draw=int(input('Sorry, '+name +' please try again. Goodluck this time around: '))
        if draw>55 or draw<65:
            print('Congratulations, '+name+' you won the grand price')
    else:
        print('Come back when you are ready')
else:
    print('Sorry, '+name + ' you are not up to age')
