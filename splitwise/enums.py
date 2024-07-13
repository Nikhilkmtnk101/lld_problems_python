from enum import Enum


class ExpenseType(Enum):
    EQUAL_EXPENSE = "EQUAL_EXPENSE"
    EXACT_EXPENSE = "EXACT_EXPENSE"
    PERCENT_EXPENSE = "PERCENT_EXPENSE"
