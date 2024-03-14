from abc import ABC, abstractmethod

from design_vending_machine.coin.coin import Coin
from vending_machine.constant import METHOD_NOT_SUPPORTED_EXCEPTION
from design_vending_machine.inventory.item import Item


class State(ABC):
    @abstractmethod
    def start_payment(self):
        pass

    @abstractmethod
    def insert_coin(self, coin: Coin):
        pass

    @abstractmethod
    def start_product_selection(self):
        pass

    @abstractmethod
    def select_product(self, code: int):
        pass

    @abstractmethod
    def dispense_product(self) -> list[Coin]:
        pass

    @abstractmethod
    def get_change(self, change_money: int) -> int:
        pass

    @abstractmethod
    def cancel_request(self):
        pass


class IdleState(State):
    def __init__(self, vending_machine):
        print("Currently Vending machine is in IdleState")
        self.vending_machine = vending_machine
        coins = []
        self.vending_machine.set_coins(coins)

    def start_payment(self):
        self.vending_machine.set_state(PaymentState(self.vending_machine))

    def insert_coin(self, coin: Coin):
        raise METHOD_NOT_SUPPORTED_EXCEPTION

    def start_product_selection(self):
        raise METHOD_NOT_SUPPORTED_EXCEPTION

    def select_product(self, code: int):
        raise METHOD_NOT_SUPPORTED_EXCEPTION

    def dispense_product(self) -> list[Coin]:
        raise METHOD_NOT_SUPPORTED_EXCEPTION

    def get_change(self, change_money: int) -> int:
        raise METHOD_NOT_SUPPORTED_EXCEPTION

    def cancel_request(self):
        raise METHOD_NOT_SUPPORTED_EXCEPTION


class PaymentState(State):
    def __init__(self, vending_machine):
        print("Currently Vending machine is in Payment State")
        self.vending_machine = vending_machine

    def start_payment(self):
        return

    def insert_coin(self, coin: Coin):
        print("Accepted the coin")
        self.vending_machine.add_coin(coin)

    def start_product_selection(self):
        self.vending_machine.set_state(ProductSelectionState(self.vending_machine))

    def select_product(self, code: int):
        raise METHOD_NOT_SUPPORTED_EXCEPTION

    def dispense_product(self) -> list[Coin]:
        raise METHOD_NOT_SUPPORTED_EXCEPTION

    def get_change(self, change_money: int) -> int:
        raise METHOD_NOT_SUPPORTED_EXCEPTION

    def cancel_request(self) -> list[Coin]:
        print("Returned the full amount back in the Coin Dispense Tray")
        self.vending_machine.set_state(IdleState(self.vending_machine))
        return self.vending_machine.get_coins()


class ProductSelectionState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def start_payment(self):
        raise METHOD_NOT_SUPPORTED_EXCEPTION

    def insert_coin(self, coin: Coin):
        raise METHOD_NOT_SUPPORTED_EXCEPTION

    def start_product_selection(self):
        return

    def select_product(self, code: int):
        item = self.vending_machine.get_inventory().get_item(code)
        money_paid_by_user = 0
        for coin in self.vending_machine.get_coins():
            money_paid_by_user += coin.value

        if money_paid_by_user < item.get_price():
            raise Exception("Insufficient Amount Paid by User")

        self.vending_machine.set_state(DispensingState(self.vending_machine, code))
        return self.get_change(money_paid_by_user-item.get_price())

    def dispense_product(self) -> list[Coin]:
        pass

    def get_change(self, change_money: int) -> int:
        print("Returning change to user: ", change_money)
        return change_money

    def cancel_request(self):
        print("Returned the full amount back in the Coin Dispense Tray")
        self.vending_machine.set_state(IdleState(self.vending_machine))
        return self.vending_machine.get_coins()


class DispensingState(State):
    def __init__(self, vending_machine, product_code: int):
        self.vending_machine = vending_machine
        self.product_code = product_code

    def start_payment(self):
        pass

    def insert_coin(self, coin: Coin):
        pass

    def start_product_selection(self):
        pass

    def select_product(self, code: int):
        pass

    def dispense_product(self) -> Item:
        print("Product has been dispensed")
        item = self.vending_machine.get_inventory().get_item(self.product_code)
        self.vending_machine.get_inventory().update_item_sold_out(self.product_code)
        self.vending_machine.set_state(IdleState(self.vending_machine))
        return item

    def get_change(self, change_money: int) -> int:
        pass

    def cancel_request(self):
        print("Returned the full amount back in the Coin Dispense Tray")
        self.vending_machine.set_state(IdleState(self.vending_machine))
        return self.vending_machine.get_coins()

