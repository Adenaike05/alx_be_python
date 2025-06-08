# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains the current date and time, and prints it in a readable format.
    """
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_date}")
    return current_date # Return current_date for use in the next function

def calculate_future_date(start_date):
    """
    Prompts the user for a number of days, calculates the future date,
    and prints it in a readable format.

    Args:
        start_date (datetime): The date from which to calculate the future date.
    """
    while True:
        try:
            days_to_add_str = input("Enter the number of days to add to the current date: ")
            days_to_add = int(days_to_add_str)
            break # Exit loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    # Calculate the future date by adding the specified number of days
    future_date = start_date + timedelta(days=days_to_add)
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    """
    Main function to run the datetime exploration script.
    """
    # Part 1: Display the current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate a future date
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()