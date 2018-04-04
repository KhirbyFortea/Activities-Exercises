#PAUL KHIRBY B. FORTEA
#github.com/KhirbyFortea
#Khirby.Fortea@gmail.com
#Guessing Game


import random

highest = 10
answer = random.randrange(highest)
guess= raw_input("Guess a number from 0 to 10: ")

while (int(guess) !=answer):
    if(int(guess) < answer):
        print "Ligwak Ganern , Taasan mo pa bh3"
    else:
        print "Ligwak Ganern , Lower pa bh3"
    guess= raw_input("Guess a number from 0 to 10: ")
raw_input("Tumpak Ganern !")
