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
cinema = Star_Cinema()
hall1 = Hall(5, 10, 1)
hall1.entry_show("show1", "Movie 1", "8:00 PM")
print("Show List in Hall 1:")
for show in hall1.show_list:
    print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
print("Seats in Hall 1:")
print(hall1.seats)
