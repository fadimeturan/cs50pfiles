
import random


while True:
    try:
        my_level= int(input("Level: "))
        if my_level>0:
            break
    except ValueError:
        pass


my_random= random.randint(1, my_level)

while True:  
    try:  
        guess = int(input("Guess: "))
        if guess>0 and guess< my_random:
            print("Too small!")
        elif guess>0 and guess> my_random:
            print("Too large!")
        elif guess<=0:
            pass
        else:
            print("Just Right!")
            break
      
    except ValueError:
        pass




    """    bu çoook daha benlik 1 kod 
    
import random

while True:
    try:
        n = int(input("Level: "))
        random_num = random.randint(1, n)
        guess = int(input("Guess: "))
        if guess < random_num:
            print("Too small!")
            continue
        elif guess > random_num:
            print("Too Large!")
            continue
        else:
            print("Just right!")
    except ValueError:
        continue
    break
"""