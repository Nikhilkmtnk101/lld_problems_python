from design_vending_machine.inventory.item_type import ItemType


class Item:
    def __init__(self, item_type: ItemType, price: int):
        self.item_type = item_type
        self.price = price

    def set_item_type(self, item_type: ItemType):
        self.item_type = item_type

    def get_item_type(self) -> ItemType:
        return self.item_type

    def set_price(self, price: int):
        self.price = price

    def get_price(self) -> int:
        return self.price

