import math

class Seating(object):
    def __init__(self, num_seats):
        self.num_seats = num_seats
        self.seats = [None] * num_seats
        self.distance = [-1] * num_seats
	self.chart = {}

    def print(self):
        print(self.seats)

    def get_farthest(self):
        last_taken_seat = -1
        for i, s in enumerate(self.seats):
            if self.seats[i] is None:
                if last_taken_seat:
            

	
    def add(self, student):
	n = get_farthest()
	self.seats[n] = student
	self.chart[student] = n

print("hello")
seating = Seating(8)
seating.print()
