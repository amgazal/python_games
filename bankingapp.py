
def show_balance(balance):
    print('Your current balance is now ${:.2f}  '.format(balance))
    print()
    ask=input('Press any key to return to the homepage for additional services: ').lower()


def deposit(balance):
    deposited_amt=float(input('How much would you want to deposit?  ' ))
    if int(deposited_amt)<0:
        print('Invalid amount')
        return 0
    else:

        balance=balance +deposited_amt
        print('You have deposited an amount of ${:.2f} into your bank account'.format(deposited_amt))
        print('Total balance is ${:.2f}'.format(balance))
        print()
        return balance


def withdraw(balance):
    amt_withdrawal=float(input("How much do you want to withdraw?  "))
    if amt_withdrawal<0:
        print('Sorry, invalid amount')
        print()
        return 0
    elif amt_withdrawal>balance:
        print('{Insufficient funds:^10}'.format(Insufficient funds))
        print('Insufficient funds')
        print('Insufficient funds')
        print()
        return 0
    else:
        nbalance=balance-amt_withdrawal
        print('Your withdrawal was successful.')
        print('You have ${:.2f} left in you account '.format(nbalance))
        print()
        return nbalance

#BankingApp
def main():
    balance=0
    is_running=True

    while is_running:
        print('************************')
        print('__Banking Program__')
        print('************************')
        print()
        print('Please choose which banking service you need today')
        print('1. Balance display')
        print('2. Amount Deposit')
        print('3. Money Withdrawal')
        print('4. Exit')
        choice=input('Kindly select from the options (1-4):  ')

        if choice=='1':
            show_balance(balance)
        elif choice=='2':
            balance=+deposit(balance)
        elif choice=='3':
            balance=withdraw(balance)
        elif choice=='4':
            is_running=False
        else:
            print('Please enter a valid option so we can help accordingly')
    print('Thank you for your time today. Keep banking with us.')

if __name__=='__main__':
    main()
