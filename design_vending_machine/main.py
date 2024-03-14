import uuid

from coin.coin import Coin
from design_vending_machine.inventory.item import Item
from design_vending_machine.inventory.item_type import ItemType
from vending_machine.vending_machine import VendingMachine


def fill_up_inventory(machine):
    new_item = None
    slots = machine.get_inventory().inventory
    for i, shelf in enumerate(slots):
        if 0 <= i < 3:
            new_item = Item(ItemType.COKE, 12)
        elif 3 <= i < 5:
            new_item = Item(ItemType.PEPSI, 9)
        elif 5 <= i < 7:
            new_item = Item(ItemType.JUICE, 13)
        elif 7 <= i < 10:
            new_item = Item(ItemType.SODA, 7)
        shelf.set_item(new_item)
        shelf.set_sold_out(False)


def display_inventory(vending_machine):
    slots = vending_machine.get_inventory().inventory
    for shelf in slots:
        print("CodeNumber:", shelf.code,
              "Item:", shelf.item.item_type.name,
              "Price:", shelf.item.price,
              "isAvailable:", not shelf.sold_out)


if __name__ == "__main__":
    vending_machine = VendingMachine(uuid.uuid4())
    try:
        print("|")
        print("filling up the inventory")
        print("|")

        fill_up_inventory(vending_machine)
        display_inventory(vending_machine)

        print("|")
        print("clicking on InsertCoinButton")
        print("|")

        vending_state = vending_machine.get_state()
        vending_state.start_payment()

        vending_state = vending_machine.get_state()
        vending_state.insert_coin(Coin.DIME)
        vending_state.insert_coin(Coin.QUARTER)
        # vending_state.insert_coin(vending_machine, Coin.NICKEL)

        print("|")
        print("clicking on ProductSelectionButton")
        print("|")
        vending_state.start_product_selection()

        vending_state = vending_machine.get_state()
        vending_state.select_product(102)
        vending_state = vending_machine.get_state()
        vending_state.dispense_product()

        display_inventory(vending_machine)

    except Exception as e:
        print(e)
        display_inventory(vending_machine)