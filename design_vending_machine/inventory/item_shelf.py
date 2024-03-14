from design_vending_machine.inventory.item import Item


class ItemShelf:
    def __init__(self, code: int):
        self.item = None
        self.code = code
        self.sold_out = True

    def set_item(self, item: Item):
        self.item = item

    def get_item(self) -> Item:
        return self.item

    def set_code(self, code: int):
        self.code = code

    def get_code(self) -> int:
        return self.code

    def set_sold_out(self, sold_out: bool):
        self.sold_out = sold_out

    def get_sold_out(self) -> bool:
        return self.sold_out
