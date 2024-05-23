"""
Problem Statement: https://workat.tech/machine-coding/practice/splitwise-problem-0kp2yneec2q2
"""
import time

from splitwise.enum import ExpenseType
from splitwise.splits.equal_split import EqualSplit
from splitwise.splits.exact_split import ExactSplit
from splitwise.splits.percent_split import PercentSplit
from splitwise.splitwise_manager import ExpenseManager

if __name__ == '__main__':
    expense_manager = ExpenseManager()
    expense_manager.add_user("User1", "Nikhil1", "email1", "phone1")
    expense_manager.add_user("User2", "Nikhil2", "email2", "phone2")
    expense_manager.add_user("User3", "Nikhil3", "email3", "phone3")
    expense_manager.add_user("User4", "Nikhil4", "email4", "phone4")

    expense_manager.show_balances()
    expense_manager.show_balance("User1")

    splits1 = [
              EqualSplit(expense_manager.users.get("User1")),
              EqualSplit(expense_manager.users.get("User2")),
              EqualSplit(expense_manager.users.get("User3")),
              EqualSplit(expense_manager.users.get("User4"))
            ]
    expense_manager.add_expense(ExpenseType.EQUAL_EXPENSE.value, 1000, expense_manager.users.get("User1"), splits1)
    expense_manager.show_balance("User4")
    expense_manager.show_balance("User1")

    splits2 = [
        ExactSplit(expense_manager.users.get("User2"), 370),
        ExactSplit(expense_manager.users.get("User3"), 880)
    ]
    expense_manager.add_expense(ExpenseType.EXACT_EXPENSE.value, 1250, expense_manager.users.get("User1"), splits2)
    expense_manager.show_balances()

    splits3 = [
        PercentSplit(expense_manager.users.get("User1"), 40),
        PercentSplit(expense_manager.users.get("User2"), 20),
        PercentSplit(expense_manager.users.get("User3"), 20),
        PercentSplit(expense_manager.users.get("User4"), 20)
    ]
    expense_manager.add_expense(ExpenseType.PERCENT_EXPENSE.value, 1200, expense_manager.users.get("User4"), splits3)
    expense_manager.show_balance("User1")
    expense_manager.show_balances()
