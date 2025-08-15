import random
print ("THE GUESS GAME")
number = range(10)
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=(int(input ("guess a number between 0 - 9: ")))
    guess_count += 1
    correct_guess = random.choice(number)
    if correct_guess==guess:
        print("WOW !!!! that was amazing. you WON\n")
        break
    else:
        print("Oooooo Noooooooo you lost the game 😢😢😢😢😢😢😢")
        print (f"The correct answer is {correct_guess}\n")
if guess_count==guess_limit:
    print ("You can't play anymore,you have exhausted all you chances")
