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

    def get_item(self, item_name):
        for item in self.current_room.room_items:
            if item.name == item_name:
                self.current_room.room_items.remove(item)
                return self.backpack.append(item)
        print(f"You put the {item.name} in your backpack.")

    def drop_item(self, item_name):
        for item in self.backpack:
            if item.name == item_name:
                self.backpack.remove(item)
                return self.current_room.room_items.append(item)
            print(f"You have dropped the {item.name} on the ground.")