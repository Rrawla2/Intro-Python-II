# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.backpack = []

    def move_player(self, direction):
        next_room = self.current_room.new_room(direction)
        if next_room is not None:
            self.current_room = next_room
            self.current_room.my_current_room()
        else:
            print(f"That is not a valid direction to travel.")

