class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        if isinstance(hall, Hall):
            self.hall_list.append(hall)
        else:
            print("Invalid object. Only objects of class Hall can be added to hall_list.")

class Hall:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

hall1 = Hall("Hall 1", 100)
hall2 = Hall("Hall 2", 150)
cinema = Star_Cinema()
cinema.entry_hall(hall1)
cinema.entry_hall(hall2)
print("Hall List:")
for hall in cinema.hall_list:
    print(f"{hall.name} - Capacity: {hall.capacity}")
