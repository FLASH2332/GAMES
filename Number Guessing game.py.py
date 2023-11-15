import random
import math
up_lim=100
low_lim=1
def guess_number():
    global low_lim
    global up_lim
    print("Enter a number between 1-100 and Remember it!")
    while(low_lim!=up_lim):
        GUESS=random.randint(low_lim,up_lim)
        guess1=input(f"Is your number greater than {GUESS}").lower()
        if(guess1=='y'):
            low_lim=GUESS+1
        if(guess1=='n'):
            #up_lim=math.ceil((up_lim+GUESS)/2)
            up_lim=GUESS
        if(up_lim-low_lim==1):
            break
        
    print("Your number is",low_lim)
guess_number()




