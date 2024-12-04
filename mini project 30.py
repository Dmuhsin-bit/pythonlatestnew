class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        """Initialize the account with an account holder name and initial balance."""
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account."""
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        """Check the current balance of the account."""
        print(f"The current balance is: ${self.balance:.2f}")
        return self.balance

# Example usage:
account = BankAccount("muhsin", 100)
account.deposit(50)
account.withdraw(30)
account.check_balance()
account.withdraw(150)
