class Star_Cinema:
    hall_list = []

    @classmethod
    def add_hall(cls, hall_object):
        if isinstance(hall_object, Hall):
            cls.hall_list.append(hall_object)
            print(f"Hall '{hall_object.hall_no}' added to the hall list.")
        else:
            print("Invalid input. Please provide an object of class 'Hall'.")

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {} 
        self.show_list = [] 
        self.create_seats() 
        self.entry_hall() 

    def create_seats(self):
        self.seats = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def entry_hall(self):
        self.add_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)
        self.seats[show_id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self, show_id, seat_list):
        if show_id not in self.seats:
            print(f"Show ID {show_id} does not exist.")
            return

        for row, col in seat_list:
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                print(f"Invalid seat: Row {row}, Col {col}")
                continue

            if self.seats[show_id][row][col] == 0:
                self.seats[show_id][row][col] = 1
                print(f"Seat booked: Row {row}, Col {col}")
            else:
                print(f"Seat already booked: Row {row}, Col {col}")

hall1 = Hall(rows=5, cols=10, hall_no=1)

hall1.entry_show(show_id=1, movie_name="Movie 1", time="10:00 AM")

seat_list_to_book = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
hall1.book_seats(show_id=1, seat_list=seat_list_to_book)

print("\nShow List:")
for show in hall1.show_list:
    print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

print("\nSeats for Show ID 1:")
for row in hall1.seats[1]:
    print(row)
