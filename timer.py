tim=input('How long do you want to set the timer, '+name+': ')
import time
for x in range(int(tim),0,-1):
    sec=x%60
    min=x//60
    hours=x//3600
    print('{:02}'.format(hours)+':{:02}'.format(min)+ ':{:02}'.format(sec))
    time.sleep(1)
print('Times up!!!!')
