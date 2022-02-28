#password generator

from random import randint
from time import sleep

def ranchar():
    symbol = ['!', '@', '#', '$', '%', '^/', '&', '*' '~', '<', '>', '/']
    number = ['1','2','3','4','5','6','7','8','9']
    letter = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

    ran_num = number[randint(0, len(number)-1)]
    ran_sym = symbol[randint(0, len(symbol)-1)]
    ran_let = letter[randint(0, len(letter)-1)]

    ran_c = [ran_num, ran_sym, ran_let]
    ran_list = ran_c[randint(0, len(ran_c)-1)]

welcome = input('Do you want to make a password: ')
if welcome == 'yes':
    sleep(2)
    password_length = int(input('How long do you want your password to be: '))
    password = []
    sleep(2)
    for x in str(password_length):
        password.append(ranchar())
    print(password)
    
elif welcome == 'no':
    no = 'Have a nice day'
    print(no)






    