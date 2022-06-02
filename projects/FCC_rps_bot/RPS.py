# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    
    guesses = ["R", "S", "P"]
    x = random.randint(0, 2)
    guess = guesses[x]
    #if len(opponent_history) > 2:
    #    guess = opponent_history[-2]

    return guess
