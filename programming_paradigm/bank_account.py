# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a new bank account with an optional initial balance.
        Default balance is 0 if not specified.
        """
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        """
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount if there are sufficient funds.
        Returns True if the withdrawal is successful, otherwise False.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
