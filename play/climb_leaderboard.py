'''
An arcade game player wants to climb to the top of the leaderboard and track their ranking.
The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number 1 on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

Ex. ranked = [100, 90, 90, 80]
player = [70, 80, 105]
The ranked players will have ranks 1, 2, 2, and 3, respectively. 
If the player's scores are 70, 80 and 105, their rankings after each game are 4, 3 and 1. Return [4, 3, 1].
returns new rank of new scores
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked_scores, player):
    player_rankings = list()
    ranked_scores = list(set(ranked_scores))
    ranked_scores.sort(reverse=True)
    i = len(ranked_scores) - 1    
    for player_score in player:
        while i >= 0:
            dense_rank = i + 1
            if player_score < ranked_scores[i]:
                player_rankings.append(dense_rank+1)
                break
            elif player_score == ranked_scores[i]:
                player_rankings.append(dense_rank)
                break
            elif player_score > ranked_scores[i] and i == 0:
                player_rankings.append(1)
                i = i+1
                break
            elif player_score > ranked_scores[i]:
                i = i-1


    
    return player_rankings

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
