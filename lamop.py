# a=0
# if a==1:
#     print('x is shut the 0')
# elif a==0:
#     print('x is still 0')
# elif a==0:
#     print('x is not 0')
print('before the if')
x_score=input('type your score  ')
y_score=500
if int(x_score) > int(y_score):
    print('inside the if')
    winner = "x"
    print('winner is '+winner)

else:
    print('inside the else')
    winner = "y"
    print('winner is '+winner)
print('after the if')
