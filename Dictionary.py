#PAUL KHIRBY B. FORTEA
#github.com/KhirbyFortea
#Khirby.Fortea@gmail.com
#EXERCISE NO. 5 - DICTIONARIES

print ("\n\t\t Cpe Laboratory Equipments \n\t\t  BASIC INFORMATION ABOUT: \n\n 1.Power Supply \n 2. Soldering Iron \n 3. Power Extension \n 4. Drill \n 5. Pliers")
def hey():
     
    khirb = {"1":"Item: Power Supply \nQuantity: 10","2":"Item: Soldering Iron \nQuantity: 18","3":"Item: Power Extension \nQuantity: 12","4":"Item: Drill \nQuantity: 5","5":"Item: Pliers \nQuantity: 12",}

    paul = input("\n Enter Item Number :  ")
    if paul == 1:
        print khirb["1"]
    elif paul == 2:
        print khirb["2"]
    elif paul == 3:
        print khirb["3"]
    elif paul == 4:
        print khirb["4"]
    elif paul == 5:
        print khirb["5"]
   
    else:
        print ("No name matched with the no. you've entered!!!")
        return hey()
    return hey()

    
hey()




