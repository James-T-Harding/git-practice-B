class Budget:
    def __init__(self, category, initial_amount):
        self.category = category
        self._balance = initial_amount

    def __repr__(self):
        return f'{self.category} - {self._balance}'

    @property
    def balance(self):
        return self._balance

    def deposit(self, deposit):
        self._balance += deposit

    def withdraw(self, withdrawal):
        if withdrawal > self._balance:
            raise ValueError(f"Withdrawal of {withdrawal} on {self} exceeded balance.")

        self._balance -= withdrawal

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)


if __name__ == "__main__":
    food = Budget("Food", 300)
    clothes = Budget("Clothes", 200)

    print(food)

    food.withdraw(50)
    print("After withdrawing 50:", food)

    print("New Budget: ", clothes)
    food.transfer(clothes, 100)
    print("Amount after transfer of 100 to Clothes: ", clothes, ":", food)
