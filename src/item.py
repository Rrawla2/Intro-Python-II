class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, item_name):
        for item in self.current_room.room_items:
            if item.name == item_name:
                self.current_room.room_items.remove(item)
                return self.backpack.append(item)
        print(f"You put the {item.name} in your backpack.")

    def on_drop(self, item_name):
        for item in self.backpack:
            if item.name == item_name:
                self.backpack.remove(item)
                return self.current_room.room_items.append(item)
            print(f"You have dropped the {item.name} on the ground.")


