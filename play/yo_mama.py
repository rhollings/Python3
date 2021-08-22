"""

Would calling this on my portfolio be appropriate?? 

"""

import sys, requests

response = requests.get("https://yomomma-api.herokuapp.com/jokes")
joke = response.json()
while True:
    print('Welcome....')
    print('=====================')

    while True:
        print("Would you like a 'yo mama' joke?")
        answer = input("y or n:  ")

        if answer == 'y':
            print('____________________')
            print(joke['joke'])
            print('=====================')


        else:
            answer == 'n'
            print('Goodbye...')
            sys.exit()
