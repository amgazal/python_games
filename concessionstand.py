
#Concession Stand
menu={'popcorn':2.49,'butter':0.99,'lemonade':5.49,'soda':3.49,'ticket':19.99,'pizza':9.99,'fries':5.49}

cart=[]
total=0
print()
print('------MENU-----')
print()
print('__Welcome to the Missing Booth Theatre __')
print('Below is what we have available for a good experience. Pease enjoy!')
print()

for x,y in menu.items():
    print('{:15}'.format(x)+': $ '+str(y))
print()
print()

while True:
    choice=input('Please let us know what you need(press q if you need nothing else): ').lower()

    if menu.get(choice):
        cart.append(choice)
    elif choice=='q':
        break
    else:
        print('Please choose from the menu above')

print()
print('Below is your cart: ')
print(cart)
print()

for item in cart:
    x=float(menu.get(item))
    total=total + x
    tax= 0.14*total
print('The total amount for your items is: $ {:.2f}'.format(total))
print('The calculated tax is: $ {:.2f}'.format(tax))
print()
print('Have a good time!')
