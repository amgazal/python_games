
#Python Slot Machine

import random
import time
import datetime

def spin_row():
    symbols=['🍒','🔔', '🍉','🥭','⭐']
    row=[]
    for x in range(3):
        a_i=random.choice(symbols)
        p=row.append(a_i)
    return row

def print_row(spin):
    time.sleep(.5)
    print('⁂⁂⁂⁂⁂')
    print('⁂⁂⁂⁂⁂⁂⁂⁂')
    print('⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂')
    print(' | '.join(spin))

def payout(bet,spin,balance):


    cash_out=0
    if spin[0]==spin[1]==spin[2]:

        if spin[0]=='🍒':
            cash_out=int(bet)*3
            return cash_out

        elif spin[0]=='🔔':
            cash_out= int(bet)*5
            return cash_out

        elif spin[0]=='🍉':
            cash_out= int(bet)*10
            return cash_out

        elif spin[0]=='🥭':
            cash_out= int(bet)*15
            return cash_out

        elif spin[0]=='⭐':
            cash_out= int(bet)*25
            return cash_out

    else:
        return 0



def main():
    start_time=time.perf_counter()
    print('****************************')
    print('This is a Python Slots Game')
    print('****************************')
    print()
    balance=100
    returns=0
    is_playing=True
    symbols=['Symbols: 🍒 🔔 🍉 🥭 ⭐']
    luck=int(input('How lucky are you feeling today on a scale of 1-5: '))
    if luck>=1:
        consent=input('Any feeling of luck is worth a spin; wouldn''t you agree?\n'+''
        'Mind trying out your luck in a slots game(y/n): ').upper().strip()
        if consent!='Y':
            print('Quite unfortunate you dont want to play.\nHave a nice day\n')

        else:
            print()
            print('<<<You get a $100 worth of spin.\nHow you choose to partition the '+
                  'money for each spin depends on you.\nAll the best>>>')
            while is_playing:

                if balance>0:
                    print()
                    time.sleep(1)
                    print('****You have $ '+str(balance)+'!!!****')
                    bet=input('How much would you like to spin: $')

                    if not bet.isdigit():
                        print('Please put in a numeric whole amount(in short, no decimals).')
                        continue

                    if int(bet)>balance:
                        print('Sorry but you dont have that amountas at this moment\n')
                        continue

                    if int(bet)<0:
                        print('Invalid input')
                        continue




                    balance-=int(bet)
                    spin=spin_row()
                    print('Spinning an amount of $'+str(bet)+'\n')
                    time.sleep(1)
                    print('⌛⏳')
                    time.sleep(1)
                    print('Spinning....')
                    time.sleep(.5)
                    print('Spinning.......')
                    time.sleep(.5)
                    print('Spinning..........')
                    print_row(spin)
                    returns=payout(int(bet),spin,balance)
                    if returns>0:
                        print('Horray!\n')
                        print('🎆🎆')
                        time.sleep(.5)
                        print('🎆🎆🎆')
                        time.sleep(1.1)
                        print('🎆🎆🎆🎆')
                        time.sleep(1.7)
                        print()
                        if spin[0]=='🍒':
                            print('Quite the Harry Porter you are, you just won a huge amount of $'+str(returns)+'.\n'
                                  'Whooo!!!\n')

                        if spin[0]=='🔔':
                            print('You, Genius, you just won a huge amount of $'+str(returns)+'.\n'+
                                  'Unbelievable!!!\n')

                        if spin[0]=='🍉':
                            print('You, Lucky vampire, you just won a huge amount of $'+str(returns)+
                                  '.\n' +'Astonishing!!!\n')


                        if spin[0]=='🥭':
                            print('You, Wizard of Oz! you just won a huge amount of $'+str(returns)+'.\n'
                                  'Vamos!!!\n')


                        if spin[0]=='⭐':
                            print('No way!!! You just won a huge amount of $'+str(returns)+'.\n'+
                                  'Incredible!!!\n')

                        leave=input('To withdraw and leave with your win, kindly press q or press any other key to '+
                            'continue: ').strip().lower()

                        if leave=='q':
                            balance+=returns
                            is_playing=False
                            print('Enjoy \n')
                            print('You leave with a fortune worth $'+str(balance)+'.\n'+'Take Care!')

                    else:
                        print('Sorry you lost this round.\nBetter luck next time\n')
                        choice=input('Would you like to try again(y/n): ').strip().upper()

                        if choice=='N':
                            is_playing=False
                            print('You leave with $'+str(balance))
                            print('Cant wait to have you again. Feel free to come around')
                            print()

                    balance+=returns








                else:
                    is_playing=False
                    time.sleep(.5)
                    print('😞')
                    time.sleep(1.5)
                    print('😞😞')
                    time.sleep(1)
                    print('You not only ran out of luck but out of money as well, huh!\n'+
                            'This looks like the end of the road\n'+
                            'More seeds of fortune to your lucky tree next time')

    else:
        print('Tough one huh!.\nEnjoy your day nonetheless.')


    end_time=time.perf_counter()
    elapsed_time=end_time-start_time
    now_time=datetime.datetime.now()
    now_time=now_time.strftime('%H:%M:%S %D')

    print('As at '+str(now_time)+' python ran for a period of '+str(elapsed_time)+'seconds.')


if __name__=='__main__':
    main()
