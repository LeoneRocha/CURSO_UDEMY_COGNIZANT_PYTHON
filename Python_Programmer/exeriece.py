
lyric = """Can't stop, addicted to the shindig
Chop top, he says I'm gonna win big
Choose not a life of imitation
Distant cousin to the reservation
Defunct, the pistol that you pay for
This punk, the feeling that you stay for
In time, I want to be your best friend
Eastside love is living on the West End
Knock out, but boy you better come to
Don't die, you know the truth is some do
Go write your message on the pavement
Burn so bright, I wonder what the wave meant
White heat is screaming in the jungle
Complete the motion if you stumble
Go ask the dust for any answers
Come back strong with 50 belly dancers"""
lyric = """Can't stop, addicted to the shindig
Chop top, he says I'm gonna win big
Choose not a life of imitation
Distant cousin to the reservation
Defunct, the pistol that you pay for
This punk, the feeling that you stay for
In time, I want to be your best friend
Eastside love is living on the West End
Knock out, but boy you better come to
Don't die, you know the truth is some do
Go write your message on the pavement
Burn so bright, I wonder what the wave meant
White heat is screaming in the jungle
Complete the motion if you stumble
Go ask the dust for any answers
Come back strong with 50 belly dancers"""

 
  
print(lyric[len(lyric)-38:])



def printtype(valor):
    if type(valor) == int:
        return "Int"
    elif type(valor) == float:
        return "Float"
    else:
        return "String"

printtype(10)


shoes = ["Spizikes","Air Force 1","Curry 2","Melo 5"]

def addfront(lista, addval):
    lista.append(addval)
    print(lista)
    
addfront(shoes, "White Vans")


shoes = ("Spizikes","Air Force 1","Curry 2","Melo 5")

def appendtotuple(thetuple, value):
    lista =list(thetuple)
    lista.append(value)  
    novatupla = tuple(lista)
    return novatupla
    

appendtotuple(shoes,"bota")


numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]

odds_1 = set(numbers)

odds = set([])

for eachnum in odds_1:
    if eachnum % 2 == 1:
        odds.add(eachnum)