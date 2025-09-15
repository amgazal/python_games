
import random
import string
print('This is a bot to help you create a password!')
u_password=input('Please tell us about your favorite fav:  ')
u_year= input('Please key in any date of your choice: ')
encrpypted= string.punctuation+ string.digits+' '+ string.ascii_letters
mod=' '
cod=' '

for letter in u_password:
    ind=u_password.index(letter)
    mod=mod+ encrpypted[ind]
for number in u_year:
    index=u_year.index(number)
    cod+=encrpypted[index]
print( 'Your password is:  '+ mod +''+cod)
