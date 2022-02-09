# Quiz Game example

print("Welcome to Quiz Game!!!")

is_playing = input("Would you like to play? (yes or no)  ")

if is_playing.lower() != 'yes':
    quit()

print("Great! Let's Play!!")

score = 0

answer = input("What color is Midoriya's hair?  ")
if answer.lower() == "green":
    print('Correct!')
    score += 1
else:
    print('Incorrect! :(')

answer = input("What is Bakugo's quirk?  ")
if answer.lower() == "explosion":
    print('Correct!')
    score += 1
else:
    print('Incorrect! :(')
    
answer = input("Who's quirk is 'Hardening'?  ")
if answer.lower() == "kirishima":
    print('Correct!')
    score += 1
else:
    print('Incorrect! :(')

answer = input("What is the school's motto?  ")
if answer.lower() == "go beyond plus ultra":
    print('Correct!')
    score += 1
else:
    print('Incorrect! :(')

answer = input("What power does shoto dislike using?  ")
if answer.lower() == "fire":
    print('Correct!')
    score += 1
else:
    print('Incorrect! :(')


print("Your score is {} out of 5".format(score))
print("You got {}%".format(score//5*100))
