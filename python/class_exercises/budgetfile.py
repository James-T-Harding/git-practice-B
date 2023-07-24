import os.path
from collections import UserList
import os


class Budget:
    """
    Encapsulates a budget object with criteria such as category and balance.
    """
    def __init__(self, category: str, initial_amount: int):
        self.category = category
        self._balance = initial_amount

    def __repr__(self):
        return f'{self.category} - {self._balance}'

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


class BudgetFile(UserList):
    def __init__(self, filename):
        self.path = f"{filename}.csv"
        super().__init__(self.read() if os.path.isfile(self.path) else None)

    def read(self):
        with open(self.path) as f:
            while line := f.readline():
                category, balance = line.strip('\n').split(',')
                budget = Budget(category, balance)

                yield budget

    def save(self):
        with open(self.path, 'w') as f:
            f.write('\n'.join(budget.csv for budget in self))
