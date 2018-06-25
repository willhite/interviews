class ExamRoom:
    def __init__(self, n):
        self.seat_chart = [None] * n
        self.position_map = {}

    # Returns the index of the seat assigned to the student with id student_id  
    def add(self, student_id):
        # print("add in:", self.seat_chart)
        n = len(self.seat_chart)
        distances = [float("inf")] * n
        # Compute left- and right-distances
        for start, finish, dx in [(0, n, 1), (n - 1, -1, -1)]:
            last_filled_seat = None
            for position in range(start, finish, dx):
                if self.seat_chart[position] is None:
                    if last_filled_seat is not None:
                        distances[position] = min(distances[position], abs(position - last_filled_seat))
                else:
                    last_filled_seat = position
            # print("distances:", distances)
        for i, d in enumerate(distances):
            if d == float("inf"):
                distances[i] = -100
        # print("distances:", distances)
        final_position = distances.index(max(distances))
        self.seat_chart[final_position] = student_id
        self.position_map[student_id] = final_position
        print("add out:", self.seat_chart)
        return final_position

    def remove(self, student_id):
        assert student_id in self.position_map
        position = self.position_map.pop(student_id)
        self.seat_chart[position] = None

    def print(self):
        print(self.seat_chart)


r = ExamRoom(8)
r.add("s1")
r.add("s2")
r.add("s3")
r.remove("s1")
r.add("s4")
r.add("s5")
