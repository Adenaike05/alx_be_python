
import sys
from bank_account import BankAccount

def main():
    """
    Parses command-line arguments to perform banking operations on a BankAccount.
    """
    # Create a BankAccount instance with an example starting balance
    # You can adjust this initial balance for different testing scenarios
    try:
        account = BankAccount(100.00)
    except ValueError as e:
        print(f"Error initializing account: {e}")
        sys.exit(1)

    # Check for minimum number of arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount_or_none>")
        print("Commands: deposit, withdraw, display")
        print("Example: python main-0.py deposit:50")
        print("Example: python main-0.py withdraw:20")
        print("Example: python main-0.py display")
        sys.exit(1)

    arg_parts = sys.argv[1].split(':', 1) # Split only on the first colon
    command = arg_parts[0].lower() # Convert command to lowercase for case-insensitivity
    
    amount_str = None
    if len(arg_parts) > 1:
        amount_str = arg_parts[1]

    amount = None
    if amount_str:
        try:
            amount = float(amount_str)
        except ValueError:
            print(f"Error: Invalid amount '{amount_str}'. Please provide a valid number.")
            sys.exit(1)

    
    if command == "deposit":
        if amount is not None:
            try:
                account.deposit(amount)
                print(f"Deposited: ${amount:.2f}")
            except ValueError as e:
                print(f"Error during deposit: {e}")
        else:
            print("Error: Deposit command requires an amount. Usage: deposit:<amount>")
    elif command == "withdraw":
        if amount is not None:
            try:
                if account.withdraw(amount):
                    print(f"Withdrew: ${amount:.2f}")
                else:
                    print("Insufficient funds.")
            except ValueError as e:
                print(f"Error during withdrawal: {e}")
        else:
            print("Error: Withdraw command requires an amount. Usage: withdraw:<amount>")
    elif command == "display":
        account.display_balance()
    else:
        print(f"Invalid command: '{command}'.")
        print("Commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()