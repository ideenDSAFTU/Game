#เกมสุ่มทายตัวเลข
print('welcome to....')
print('Game guessing the number for fun')
print('********************')
name = str(input('Please enter your name :    '))
print('...........................')
import random
from unicodedata import name
x = random.randint(1,20)
a = -1
while(a !=x):
    a = int(input('Guess the numbers 0 to 19 : '))
    if a == x :
        print('Congratulations, you are right')
    else:
        if a < x :
            print('It is too low numbers,Please try again.')
            print('...........................')
        else:
            print('It is too hight numbers, please try again.')
            print('...........................')   