#PAUL KHIRBY B. FORTEA
#github.com/KhirbyFortea
#Khirby.Fortea@gmail.com
#Calculator



def menu():
    #print what options you have
    print "Welcome to calculator in Python"
    print "your options are:"
    print " "
    print "1) Addition"
    print "2) Subtraction"
    print "3) Multiplication"
    print "4) Division"
    print "5) Quit calculator"
    print " "
    return input ("Choose your option: ")

# Adds two numbers given
def add(a,b):
    print a, "+", b, "=", a + b

# Subtracts two numbers given
def sub(a,b):
    print b, "-", a, "=", b - a

# Multiplies two numbers given
def mul(a,b):
    print a, "*", b, "=", a * b

# Divides two numbers given
def div(a,b):
    print a, "/", b, "=", a / b

# NOW THE PROGRAM STARTS, AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(input("Add this number: "),input("to this number: "))
    elif choice == 2:
        sub(input("Subtract this number: "),input("from this number:  "))
    elif choice == 3:
        mul(input("Multiply this number: "),input("by this number: "))
    elif choice == 4:
        div(input("Divide this number: "),input("by this number: "))
    elif choice == 5:
        loop = 0

print "Thankyou for using calculator!"

# End of the program
