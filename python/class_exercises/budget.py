from typing import List


class Budget:
    """
    Encapsulates a budget object with criteria such as category and balance.
    """
    def __init__(self, category: str, initial_amount: int, file=None):
        self.category = category
        self.file = file
        self._balance = initial_amount

        self._id = None

    def __repr__(self):
        return f'{self.category} - {self._balance}'

    def __bool__(self):
        return self._id or self.category or self.balance

    @property
    def is_saved(self):
        """
        Budget is saved to file, determined by whether an id has been declared.
        """
        return self._id is not None

    @property
    def balance(self):
        return self._balance

    @property
    def bd(self):
        """
        Property that generates a string to write to a file.
        """
        return (
            f"{self._id:<{self.file.ID}}"
            f"{self.category:<{self.file.CATEGORY}}"
            f"{self.balance:<{self.file.BALANCE}}"
        )

    def assign_id(self, value):
        if not self.file:
            raise OSError(f"No associated Budget file for {self}")

        self._id = value

    def save(self):
        if not self.file:
            raise OSError(f"No associated file for {self}")

        if self.is_saved:
            self.file.goto(self._id - 1)
            self.file.write(self.bd)

        else:
            self.file.goto_end()
            self._id = self.file.increment_entries()
            self.file.write(self.bd)
            self.file.newline()

    def deposit(self, deposit: int):
        """
        Increases balance by a set amount.
        """
        self._balance += deposit

    def withdraw(self, withdrawal: int):
        """
        Decreases balance by a supplied amount.
        """
        if withdrawal > self._balance:
            raise ValueError(f"Withdrawal of {withdrawal} on {self} exceeded balance.")

        self._balance -= withdrawal

    def transfer(self, other, amount: int):
        """
        Transfers balance from self into other.
        """

        self.withdraw(amount)
        other.deposit(amount)


class BudgetFile:
    ID = 4
    CATEGORY = 16
    BALANCE = 4
    LINE_LENGTH = ID + CATEGORY + BALANCE + 1

    # HEADER VARS
    ENTRY_LENGTH = 4
    HEADER_LENGTH = ENTRY_LENGTH + 1

    """
    Object that encapsulates a budget file.
    ...
    Atttributes
    ----------
    filename : str
        The name of the budget file.
    """

    def __init__(self, filename: str):
        """
        filename: str
            The name of the budget file.
        """
        try:
            self.file = open(f"{filename}.bd", 'x')
            header = f"{0:<{self.ENTRY_LENGTH}}\n"
            self.file.write(header)

        except FileExistsError:
            self.file = open(f"{filename}.bd", 'r+')
            header = self.file.readline()

        self.entries = int(header)

    def load_all(self) -> List[Budget]:
        """
        Loads all saved budgets.
        :returns List[Budget]
        """
        return [self.load(n) for n in range(self.entries)]

    def load(self, n: int) -> Budget:
        """
        Loads a specific budget from line n.

        :param n: int
        :return: Budget
        """

        self.goto(n)
        return self._read_budget()

    def close(self) -> None:
        """
        Saves and closes the file
        """
        self.file.seek(0)
        self.file.write(f"{self.entries:<{self.ENTRY_LENGTH}}")
        self.file.close()

    def increment_entries(self) -> int:
        self.entries += 1
        return self.entries

    def goto(self, line: int):
        """
        Goes to the specified line.
        """
        self.file.seek(self.HEADER_LENGTH + line * self.LINE_LENGTH)

    def newline(self):
        """
        Prints a newline symbol.
        :return:
        """
        self.file.write('\n')

    def goto_end(self):
        self.goto(self.entries)

    def write(self, line: str):
        self.file.write(line)

    def _read_id(self):
        return int(self.file.read(self.ID))

    def _read_category(self):
        return self.file.read(self.CATEGORY).strip()

    def _read_balance(self):
        return int(self.file.read(self.BALANCE))

    def _read_budget(self) -> Budget:
        budget_id = self._read_id()
        category = self._read_category()
        balance = self._read_balance()

        budget = Budget(category, balance, self)
        budget.assign_id(budget_id)

        return budget


def main():
    file = BudgetFile("budget")
    clothes = Budget("clothes", 100, file)
    clothes.save()
    file.close()


if __name__ == "__main__":
    main()
