import time
 
lives = 5
stringword = "Apple"
word = list(stringword.lower())
guess = ["_"] * len(word)
winner = False
incorrectletters = []
 
def printscore():
    print("\n\nLives: " + str(lives))
    print("Incorrect Letters: ", end="")
    for x in range(len(incorrectletters)):
        if x == len(incorrectletters) - 1:
            print(incorrectletters[x], end="")
        else:
            print(incorrectletters[x], end=",")
    print("")
    for x in range(len(guess)):
        if x == len(guess) - 1:
            print(guess[x], end="")
        else:
            print(guess[x], end=",")
    print("")
 
def askforletter():
    letterguess = input("Please guess a letter: ").lower()
    correct = False
    for x in range(len(word)):
        if letterguess == word[x]:
            guess[x] = letterguess
            correct = True
    if correct:
        print("You got one! 🤓")
    else:
        print("Oh no! That wasn't in there 😕")
        incorrectletters.append(letterguess)
        global lives
        lives -= 1
    time.sleep(1)
 
def checkwinner():
    if "_" not in guess:
        global winner
        winner = True
 
while lives > 0 and winner == False:
    # Print out the current scoreboard
    printscore()
 
    # Ask the user for a letter
    askforletter()
 
    # Check if they won
    checkwinner()
 
 
if lives <= 0:
    print("You lost 😞. The word was " + stringword)
else:
    print("Congrats! You won with " + str(lives) + " lives left!")