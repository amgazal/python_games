

#PYthon SLot MAchine
import random as r
import time


def spin_row():
    symbols=['🍒','🔔','🍉','🥭','⭐']
    spin=[]

    for x in range(3):
        p=r.choice(symbols)
        spin.append(p)
    return spin




def print_row(row):
    time.sleep(.5)
    print('※※※※※※※※※※※※')
    print(' | '.join(row))
    time.sleep(1)
    print('※※※※※※※※※※※※')



def payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return 3*int(bet)
        elif row[0]=='🔔':
            return 5*int(bet)
        elif row[0]=='🍉':
            return 10*int(bet)
        elif row[0]=='🥭':
            return 15*int(bet)
        elif row[0]=='⭐':
            return 25*int(bet)
    return 0





def main():
    balance=100


    print('*****************************')

    print('This is a Python Slots game')

    print('Symbols: 🍒 🔔 🍉 🥭 ⭐')

    print('*****************************')

    print()
    while balance>0:

        print('Current Balance: $ '+str(balance))
        bet=input('How much would you want to spin? ')
        if not bet.isdigit():

            print('Please type in a whole number value')
            continue

        if int(bet)>balance:

            print('Insufficient funds!')
            continue


        if int(bet)<1:

            print('Bet should be a dollar or more')
            continue


        balance=balance-int(bet)


        row=spin_row()
        print('Spinning an amount of $'+bet)
        time.sleep(1)
        print("Spinning...\n")
        print_row(row)
        returns=payout(row,bet)
        if int(returns)>0:
            time.sleep(.5)
            print('🎆🎇')
            time.sleep(.5)
            print('🎆🎇🎆🎇')
            time.sleep(.5)
            print('🎆🎇🎆🎇🎆🎇')
            print('You won $'+str(returns))
            balance=balance+int(returns)
        else:
            print('Sorry you lost this round.')
        print()

        play_on=input('Would you like to play again(Y/N):').capitalize()
        if play_on!='Y':
            if balance<0:
                print('Better luck next time')
            else:
                print('See you again!')

            break
        else:
            if balance<=0:
                print('Sorry you ran out of money')




if __name__=='__main__':
    main()
