import os


class Budget:
    """
    Encapsulates a budget object with criteria such as category and balance.
    """
    def __init__(self, category: str, initial_amount: int):
        self.category = category
        self._balance = initial_amount

    def __str__(self):
        return f'{self.category} - {self.balance}'

    def __repr__(self):
        return f"Budget({self._category}, {self._balance})"

    @property
    def category(self):
        return self._category.title().replace('_', ' ')

    @category.setter
    def category(self, value: str):
        self._category = value.lower().replace(" ", "_")

    @property
    def category_internal(self):
        return self._category

    @classmethod
    def from_csv(cls, line):
        category, budget = line.split(',')
        return cls(category, int(budget))

    @property
    def balance(self) -> int:
        return self._balance

    @property
    def csv(self) -> str:
        return f"{self._category},{self._balance}"

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
        self.filename = filename
        self.path = f"{filename}.csv"

        if os.path.isfile(self.path):
            self.load()

    def __str__(self):
        return " ".join(map(str, self.budgets.values()))

    def __repr__(self):
        return f"BudgetFile({self.filename})"

    def __getattr__(self, item):
        return self.budgets[item]

    def add(self, budget: Budget):
        self.budgets[budget.category_internal] = budget

    def load(self):
        self.budgets.clear()

        with open(self.path) as file:
            for line in file:
                budget = Budget.from_csv(line.strip('\n'))
                self.add(budget)

    def save(self):
        with open(self.path, 'w') as f:
            for budget in self.budgets.values():
                f.write(budget.csv)
                f.write("\n")


def run():
    file = BudgetFile("budget")
    print(file)


if __name__ == "__main__":
    run()


