#PAUL KHIRBY B. FORTEA
#github.com/KhirbyFortea
#Khirby.Fortea@gmail.com
#File Handling

text_file = open("text.txt",'w')
text_file.write("Hi ! Welcome to Python !")
text_file.close()
text_file = open("text.txt",'a')
text_file.write(" in Data Structure")
text_file.close()


# to display in run!
# text_file = open("text.txt",'r')
# print(text_file.read())
# text_file.close()
