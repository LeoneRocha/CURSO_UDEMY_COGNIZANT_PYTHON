
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


x = 1
y = 1000000000

while 2**x < y:
    x = x + 1
    if 2**x > y:
        print (x)

nums = [99, 20, 30, 35, 16, 49, 39, 11, 69, 48, 85, 32, 10, 47, 24, 80, 37, 21, 3, 99, 13, 11, 23, 12, 40, 50, 24, 14, 10, 62, 21, 24, 55, 57, 38, 55, 83, 63, 34, 31, 15, 26, 82, 47, 37, 14, 64, 72, 90, 39, 70, 50, 67, 61, 23, 28, 30, 13, 87, 58, 80, 62, 15, 49, 33, 7, 38, 2, 92, 76, 80, 18, 6, 25, 22, 25, 91, 9, 37, 83, 46, 98, 69, 3, 40, 6, 48, 1, 63, 51, 32, 19, 77, 74, 22, 75, 41, 19, 27, 82, 60, 6, 1, 55, 5, 71, 18, 84, 47, 16, 1, 8, 41, 6, 17, 100, 62, 36, 45, 32, 4, 33, 68, 15, 2, 92, 50, 54, 34, 12, 17, 16, 74, 95, 2, 61, 75, 12, 6, 39, 28, 18, 30, 39, 8, 34, 62, 31, 57, 8, 69, 19, 71, 70, 40, 79, 76, 96, 84, 76, 85, 4, 40, 64, 45, 11, 46, 100, 56, 9, 86, 5, 78, 81, 18, 70, 76, 46, 85, 69, 64, 88, 17, 91, 49, 93, 18, 29, 38, 42, 77, 63, 46, 32, 83, 88, 48, 68, 89, 80]

for idx, num in enumerate(nums):
    if num == 68:
        print(idx)
        break