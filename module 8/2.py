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
        Star_Cinema.hall_list.append(self)
cinema = Star_Cinema()
hall1 = Hall(5, 10, 1)
print("Hall List in Star_Cinema:")
for hall in cinema.hall_list:
    print(f"Hall No: {hall.hall_no}, Rows: {hall.rows}, Cols: {hall.cols}")

