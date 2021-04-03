#lotto number generator

import random
import sys

while True:
    print("Lucky Lotto Number Generator")
    while True:
        print("Would you like to play?")
        play = input("y or n?")
        lotto = []
        lucky_num = []
        if play == "y":
            for i in range(0,5): #adjust amount of numbers printed here!!
                n = random.randint(0,51) #adjust range of numbers here!!
                lotto.append(n)
                
            print("Your numbers are ", lotto)
            
            for i in range(0,2): #adjust lucky/star numbers here!!
                x = random.randint(0, 13) #adjust range here!! 🤩
                lucky_num.append(x)
            print("And your lucky numbers are", lucky_num)
            print()
        else:
            play == "n"
            sys.exit()
