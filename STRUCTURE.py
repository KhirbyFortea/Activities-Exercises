#PAUL KHIRBY B. FORTEA
#github.com/KhirbyFortea
#Khirby.Fortea@gmail.com
#Structure


letters = ['p','a','u','l','k','h','i','r',
                'b','y','b','e','r','t','u','m',
                'e','n','f','o','r','t','e',
                'a','g','a','n','d','a','p','p']


from collections import Counter
letters_counts = Counter(letters)
repeat = letters_counts.most_common(5)
print ("letters repeated")
print(repeat)
