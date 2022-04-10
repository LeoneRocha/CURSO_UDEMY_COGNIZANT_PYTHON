#Hangman Project 2

used=""
letter=""
strikes=0
word="eggplant"
word=list(word)
lenword=len(word)
answer=[]

for j in range(lenword):
    answer.append(" ")
    print("Let's play Hangman. You're allowed 5 incorrect guesses")

while answer!=word and strikes<5:
    if len(used)>0:
       print("Used Letters:"+used)
       print("You have "+str(strikes)+" strikes, gimme your best guess:")

    letter=input().lower()
    if letter in answer or letter in used:
        print("You guessed that already dummy")
        continue

    if letter in word:
        element=word.index(letter)

    while element>=0:
        print("Corret!")

        answer[element]=letter
        try:
            element=word.index(letter,element+1,lenword)

        except ValueError:
            element=-1
            print(answer)

        else:
            used=used+letter
            strikes+=1
            print("Oh no! Incorrect guess -->"+letter)
            if answer==word:    
                print("Holy cow!, you won!😎")
            else:
                print("Sorry, you stink at hangman 😢")

