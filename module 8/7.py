class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        if isinstance(hall, Hall):
            self.hall_list.append(hall)
        else:
            print("Invalid object. Only objects of class Hall can be added to hall_list.")

class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}  
        self.show_list = [] 
        self.seats = {f'id_{hall_no}': [['Free' for _ in range(cols)] for _ in range(rows)}
        Star_Cinema.hall_list.append(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

    def book_seats(self, show_id, seat_list):
        if show_id in self.seats:
            for seat in seat_list:
                row, col = seat
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    if self.seats[show_id][row][col] == 'Free':
                        self.seats[show_id][row][col] = 'Booked'
                        print(f"Seat ({row}, {col}) has been booked for show {show_id}.")
                    else:
                        print(f"Seat ({row}, {col}) is already booked for show {show_id}.")
                else:
                    print(f"Seat ({row}, {col}) is invalid for this hall.")
        else:
            print(f"Show ID {show_id} not found in this hall.")

    def view_available_seats(self, show_id):
        if show_id in self.seats:
            print(f"Available seats for show {show_id}:")
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.seats[show_id][row][col] == 'Free':
                        print(f"Seat ({row}, {col}) is available.")
        else:
            print(f"Show ID {show_id} not found in this hall.")

class Counter:
    def __init__(self, hall_no):
        self.hall_no = hall_no

    def view_all_shows(self):
        hall = self.get_hall()
        if hall:
            print(f"Shows running in Hall {self.hall_no}:")
            for show in hall.show_list:
                print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        hall = self.get_hall()
        if hall:
            hall.view_available_seats(show_id)
        else:
            print(f"Hall {self.hall_no} not found.")

    def book_tickets(self, show_id, seat_list):
        hall = self.get_hall()
        if hall:
            hall.book_seats(show_id, seat_list)
        else:
            print(f"Hall {self.hall_no} not found.")

    def get_hall(self):
        for hall in Star_Cinema.hall_list:
            if hall.hall_no == self.hall_no:
                return hall
        return None
cinema = Star_Cinema()
hall1 = Hall(5, 10, 1)
hall1.entry_show("show1", "Movie 1", "8:00 PM")
hall1.entry_show("show2", "Movie 2", "6:30 PM")
counter1 = Counter(1)
counter1.view_all_shows()
counter1.view_available_seats("show1")
counter1.book_tickets("show1", [(0, 0), (0, 1)])
counter1.book_tickets("show1", [(0, 1), (1, 1])
print("Seats in Hall 1 for show1:")
print(hall1.seats["show1"])
