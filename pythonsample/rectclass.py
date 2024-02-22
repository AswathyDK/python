class Room:
    def _init_(self, area):
        self.area = area

class Flat(Room):
    def _init_(self, no_of_rooms, location):
        super()._init_(no_of_rooms * self.calculate_room_area())  
        self.no_of_rooms = no_of_rooms
        self.location = location

    def calculate_room_area(self):
        return self.no_of_rooms+ self.location
    def _eq_(self, other):
        return self.area == other.area

# Example usage:
flat1 = Flat(3, 2)
flat2 = Flat(2, 2)

if flat1 == flat2:
    print("The flats have the same area.")
else:
    print("The flats have different areas.")