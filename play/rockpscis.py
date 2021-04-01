import random, sys
#import modules needed to run in idle

print('ROCK, PAPER, SCISSORS !!!!')

#initaite varibales for score
wins = 0
loss = 0
ties = 0


while True: #main game loop
  print('%s Wins, %s Losses, %s Ties' % (wins, loss, ties)) #keeps track of score
  while True: #player loop
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    playerMove = input()
    if playerMove == 'q':
      sys.exit() #exits program
     
    if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
      break
    print('Choose r, p, s, or q.') #for different input
    
  if playerMove == 'r':
    print('ROCK vs ...')
  elif playerMove == 'p':
    print('PAPER vs...')
  elif playerMove == 's':
    print('SCISSORS vs...')
    
    #computer
  randomNumber = random.randint(1, 3)
  if randomNumber == 1:
    computerMove = 'r'
    print('ROCK')
  elif randomNumber == 2:
    computerMove = 'p'
    print('PAPER')
  elif randomNumber == 3:
    computerMove = 's'
    print('SCISSORS')
      
