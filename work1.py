class PiggyBank:
    def __init__(self, name, coins=0):
        self.name = name
        self._coins = 0
        self.put_in(coins)

    def put_in(self, amount):
        if amount <= 0:
            raise ValueError("Add real money")
        self._coins += amount

    def take_out(self, amount):
        if amount > self._coins:
            raise ValueError("Not enough money")
        self._coins -= amount

    def check_balance(self):
        return self._coins

# Create piggy bank with initial coins
pius = PiggyBank("Pius", 50000)
print(pius.check_balance())  # Output: 50000