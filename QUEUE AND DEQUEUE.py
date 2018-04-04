#PAUL KHIRBY B. FORTEA
#github.com/KhirbyFortea
#Khirby.Fortea@gmail.com
#Queue and Dequeue


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def printqueue(self):
        for items in self.items:
            print (items)

q = Queue()
print(q.isEmpty())
q.enqueue(5)
q.enqueue(15)
q.enqueue(30)
q.enqueue(45)
q.enqueue(60)
q.enqueue(75)
q.printqueue()
q.dequeue()
print("\n")
q.printqueue()
