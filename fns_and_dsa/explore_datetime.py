from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time."""
    current_date = datetime.now()
    # Formatting the date and time in a readable format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """Calculate and display a future date based on user input."""
    # Prompting the user for the number of days to add
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        # Adding the specified number of days to the current date
        future_date = current_date + timedelta(days=number_of_days)
        # Formatting the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    # Display the current date and time
    display_current_datetime()
    # Calculate and display the future date
    calculate_future_date()