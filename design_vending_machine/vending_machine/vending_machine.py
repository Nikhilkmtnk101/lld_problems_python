from uuid import UUID

from design_vending_machine.coin.coin import Coin
from design_vending_machine.inventory.inventory import Inventory
from vending_machine.constant import INVENTORY_SIZE


class VendingMachine:
    def __init__(self, machine_id: UUID):
        self.machine_id = machine_id
        self.inventory = Inventory(INVENTORY_SIZE)
        self.coins = []
        self.state = None

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory: Inventory):
        self.inventory = Inventory

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def add_coin(self, coin: Coin):
        self.coins.append(coin)

    def set_coins(self, coins: list[Coin]):
        self.coins = coins

    def get_coins(self) -> list[Coin]:
        return self.coins

