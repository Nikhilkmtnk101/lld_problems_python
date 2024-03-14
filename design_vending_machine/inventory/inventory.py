from design_vending_machine.inventory.item import Item
from design_vending_machine.inventory.item_shelf import ItemShelf


class Inventory:
    def __init__(self, inventory_size: int):
        self.inventory = []
        self._initialize_empty_inventory(inventory_size)

    def _initialize_empty_inventory(self, inventory_size: int):
        code = 101

        for i in range(0, inventory_size):
            self.inventory.append(ItemShelf(code))
            code += 1

    def add_item(self, item: Item, position: int):

        for item_shelf in self.inventory:
            if item_shelf.get_code() == position:
                if item_shelf.get_sold_out():
                    item_shelf.set_item(item)
                    item_shelf.set_sold_out(False)
                else:
                    raise Exception("already item is present, you can not add item here")

        raise Exception("Invalid Code")

    def get_item(self, position: int) -> Item:
        for item_shelf in self.inventory:
            if item_shelf.get_code() == position:
                if item_shelf.get_sold_out():
                    raise Exception("item already sold out")
                else:
                    return item_shelf.get_item()

        raise Exception("Invalid Code")

    def update_item_sold_out(self, position: int):
        for item_shelf in self.inventory:
            if item_shelf.get_code() == position:
                if item_shelf.get_sold_out():
                    raise Exception("item already sold out")
                else:
                    item_shelf.set_sold_out(True)

        raise Exception("Invalid Code")
