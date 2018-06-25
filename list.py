import random

class CircularListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = self
    
    def print(self):
        n = self.next
        print(self.data, end='')
        while n != self:
            print(" ->", n.data, end='')
            n = n.next
        print()
            
    def append(self, data):
        n = self.next
        prev = self
        while n != self:
            if prev.data <= data and data <= n.data:
                break;
            if prev.data > n.data and (prev.data < data or n.data > data):
                break;
            prev = n
            n = n.next
        new = CircularListNode(data)
        prev.next = new
        new.next = n
            

for i in range(5):
    test = list(range(-10,10))
    random.shuffle(test)
    print("testing:", test)
    clist = CircularListNode(test[0])
    for d in test[1:]:
        clist.append(d)
    clist.print()

