

class BankAccount:
    

    def __init__(self, initial_balance=0):
      
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.__account_balance = initial_balance  # Encapsulation: using double underscore

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.__account_balance += amount
        # print(f"Deposited: ${amount:.2f}") # This print is handled in main-0.py
        # print(f"New balance: ${self.__account_balance:.2f}") # For internal testing

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if the withdrawal was successful, False otherwise (insufficient funds).
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            # print(f"Withdrew: ${amount:.2f}") # This print is handled in main-0.py
            # print(f"New balance: ${self.__account_balance:.2f}") # For internal testing
            return True
        else:
            # print("Insufficient funds.") # This print is handled in main-0.py
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

if __name__ == "__main__":
    my_account = BankAccount(500)
    my_account.display_balance()

    my_account.deposit(100)
    my_account.display_balance()

    my_account.withdraw(50)
    my_account.display_balance()

    if not my_account.withdraw(1000):
        print("Tried to withdraw too much.")
    my_account.display_balance()
