from collections import UserDict, UserList
import os


class Budget:
    """
    Encapsulates a budget object with criteria such as category and balance.
    """
    def __init__(self, category: str, initial_amount: int):
        self.category = category
        self._balance = initial_amount

    def __str__(self):
        return f'{self.category} - {self._balance}'

    def __repr__(self):
        return f"Budget({self.category}, {self._balance})"

    @classmethod
    def from_csv(cls, line):
        return cls(*line.split(','))

    @property
    def balance(self) -> int:
        return self._balance

    @property
    def csv(self) -> str:
        return f"{self.category},{self._balance}"

    def deposit(self, deposit: int) -> None:
        """
        Increases balance by a set amount.
        """
        self._balance += deposit

    def withdraw(self, withdrawal: int) -> None:
        """
        Decreases balance by a supplied amount.
        """
        if withdrawal > self._balance:
            raise ValueError(f"Withdrawal of {withdrawal} on {self} exceeded balance.")

        self._balance -= withdrawal

    def transfer(self, other, amount: int) -> None:
        """
        Transfers balance from self into other.
        """

        self.withdraw(amount)
        other.deposit(amount)


class BudgetFile:
    def __init__(self, filename):
        self.budgets = {}
        self.path = f"{filename}.csv"

        if os.path.isfile(self.path):
            self.load()

    def __getattr__(self, item):
        return self.budgets[item]

    def __setattr__(self, key, value):
        self.budgets[key] = Budget(key, value)

    def load(self):
        with open(self.path, newline='') as file:
            self.budgets = {budget.category: budget for budget in map(Budget.from_csv, file)}

    def save(self):
        with open(self.path, 'w') as f:
            for budget in self.budgets.values():
                f.write(budget.csv)
                f.write("\n")
