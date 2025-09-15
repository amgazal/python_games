#Concession Stand
menu={'popcorn':'2.49','butter':'0.99','lemonade':'5.49','soda':'3.49','ticket':'19.99','pizza':'9.99','fries':'5.49'}

cart=[]
total=0
print()
print('------MENU-----')
print()
for x,y in menu.items():
    print(x+':'+y)


while True:
    choice=input('Please let us know what you need(press q if you need nothing else): ').lower()

    if choice='q'
        break
    elif choice in menu.keys()=='None':
        print('Please choose from our menu')
    else:
        cart=cart.append(choice)
print()
print('Below is your cart: ')
print(cart)
