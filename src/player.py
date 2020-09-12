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
            if self.current_room.room_items != None:
                self.current_room = next_room
                self.current_room.my_current_room()
            else:
                self.current_room = next_room
        else:
            print(f"That is not a valid direction to travel.")

    def get_item(self, item):
        for item in self.current_room.room_items:
            self.current_room.room_items.remove(item)
            print(f"You put the {item.name} in your backpack.")
            return self.backpack.append(item)

    def drop_item(self, item):
        for item in self.backpack:
            self.backpack.remove(item)
            print(f"You have dropped the {item.name} on the ground.")
            return self.current_room.room_items.append(item)

    def open_backpack(self, item):
        print("Backpack contains:")
        for item in self.backpack:
            print(f"    *{item.name}")
        print("-" * 50)