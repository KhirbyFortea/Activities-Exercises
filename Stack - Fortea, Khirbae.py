#PAUL KHIRBY B. FORTEA
#github.com/KhirbyFortea
#Khirby.Fortea@gmail.com
#My Playslist
#This program sorts my playlist by name in alphabetical order or by time 


class Stack:
    def __init__(self):
        self.items = ["Hall of Fame by The Script",
                      "Unwell by Matchbox20",
                      "The Man Who Can't Be Moved by The Script",
                      "Superheroes by The Script",
                      "Shut Up and Dance by Walk The Moon",
                      "Breakeven by The Script",
                      "Say you won't let go by James Arthur",
                      "Attention by Charlie Puth",
                      "Summer by Calvin Harris",]
        self.items2 = sorted(self.items)  
        self.items3 = self.items2[::-1]   

    def sort(self):
        return sorted(self.items2)
    def reverse(self):
        return self.items2[::-1]
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peekname(self):
        return self.items3[len(self.items)-1]
    def peeknamenext(self):
        return self.items3[len(self.items)-2]
    def peektime(self):
        return self.items[len(self.items)-1]
    def peektimenext(self):
        return self.items[len(self.items)-2]
    def size(self):
        return len(self.items)




if __name__ == "__main__":
    khirbae = Stack()
    print "Welcome to My Playlist"
    print "My Playlist has",khirbae.size(),"songs"
    x = input("Sort by:\n1. Name\n2.Time\n\tEnter your choice: ")
    if x == 1:
        while khirbae.size() >= 2:
            print "Currently playing ",khirbae.peekname()
            print "Next song is ",khirbae.peeknamenext(), "\n - - - - - - - - - - - - - - - - - - "
            khirbae.pop()
    elif x == 2:
        while khirbae.size() >= 2:
            print "Now Playing ",khirbae.peektime()
            print "Next song is ", khirbae.peektimenext(), "\n - - - - - - - - - - - - - - - - - - "
            khirbae.pop()
    else:
        print "INVALID SORTING"



