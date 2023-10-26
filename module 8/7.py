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
        self.__show_list = []  
        self.create_seats() 
        self.entry_hall() 

    def create_seats(self):
        self.seats = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def entry_hall(self):
        self.add_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.__show_list.append(show_info)
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

    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print(f"Show ID {show_id} does not exist.")
            return

        print(f"Available Seats for Show ID {show_id}:")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[show_id][row][col] == 0:
                    print(f"Row {row}, Col {col} - Available")
                else:
                    print(f"Row {row}, Col {col} - Booked")

class Counter:
    def __init__(self):
        self.hall_objects = Star_Cinema.hall_list

    def view_all_shows(self):
        for hall in self.hall_objects:
            hall.view_show_list()

    def view_available_seats(self, show_id):
        for hall in self.hall_objects:
            hall.view_available_seats(show_id)

    def book_tickets(self, show_id, seat_list):
        for hall in self.hall_objects:
            hall.book_seats(show_id, seat_list)

hall1 = Hall(rows=5, cols=10, hall_no=1)
hall1.entry_show(show_id=1, movie_name="Movie 1", time="10:00 AM")
counter = Counter()
counter.view_all_shows()
counter.view_available_seats(show_id=1)
seat_list_to_book = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
counter.book_tickets(show_id=1, seat_list=seat_list_to_book)
