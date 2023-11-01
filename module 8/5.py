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

    def view_show_list(self):
        print(f"Shows running in Hall {self.hall_no}:")
        for show in self.show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

cinema = Star_Cinema()
hall1 = Hall(5, 10, 1)
hall1.entry_show("show1", "Movie 1", "8:00 PM")
hall1.entry_show("show2", "Movie 2", "6:30 PM")
hall1.view_show_list()
