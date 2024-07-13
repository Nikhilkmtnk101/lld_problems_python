from entities.split.equal_split import EqualSplit
from entities.split.exact_split import ExactSplit
from entities.split.percent_split import PercentSplit
from splitwise.splitwise_app import SplitWise

if __name__ == '__main__':
    split_wise = SplitWise()

    "Add Users"
    split_wise.create_user("User1", "Phone1", "Email1")
    split_wise.create_user("User2", "Phone2", "Email2")
    split_wise.create_user("User3", "Phone3", "Email3")
    split_wise.create_user("User4", "Phone4", "Email4")

    "Commands"
    split_wise.get_balance()
    split_wise.get_balance_by_user_id(1)
    splits = [EqualSplit(1), EqualSplit(2), EqualSplit(3), EqualSplit(4)]
    split_wise.create_expense(1, 1000, "EQUAL_EXPENSE", splits)
    split_wise.get_balance_by_user_id(4)
    split_wise.get_balance_by_user_id(1)
    splits = [ExactSplit(2, 370), ExactSplit(3, 880)]
    split_wise.create_expense(1, 1250, "EXACT_EXPENSE",splits)
    splits = [PercentSplit(1, 40), PercentSplit(2, 20), PercentSplit(3, 20), PercentSplit(4, 20)]
    split_wise.create_expense(4, 1200, "PERCENT_EXPENSE", splits)
    split_wise.get_balance_by_user_id(1)
    split_wise.get_balance()
