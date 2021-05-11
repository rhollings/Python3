#movie night
import random
import sys

movies = ['Action & Adventure', 'Popular', 'Anime', 'Classic', 'Comedy', 'Horror', 'Thriller']
number1 = random.randint(1, 15)
number2 = random.randint(1, 20)

while True:
    print('================'*3)
    print("Movie Picker!!")
    while True:
        print("Would you like to watch a movie?? (y, n)")
        word = input()
        if word == 'n':
            sys.exit()
        if word == 'y':
            break
    print('Go to genre: ',random.choice(movies))
    print('Go down {} rows'.format(number1))
    print('And go right {} times'.format(number2))
    print('This is your movie!!')

    print("================"*3)
