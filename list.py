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
        next = self.next
        prev = self
        # find the spot to insert the new node
        while next != self:
            # is it somewhere int the middle of the list
            if prev.data <= data and data <= next.data:
                break
            # is it where the node wraps around
            if prev.data > next.data and (prev.data < data or next.data > data):
                break
            prev = next
            next = next.next
        new = CircularListNode(data)
        prev.next = new
        new.next = next
            

for i in range(5):
    test = list(range(-10, 10))
    random.shuffle(test)
    print("testing:", test)
    clist = CircularListNode(test[0])
    for d in test[1:]:
        clist.append(d)
    clist.print()

