# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program
def main():
    """
    Main function to interact with the user and perform temperature conversions.
    """
    print("Temperature Conversion Tool")
    while True:
        try:
            # Prompt the user to enter the temperature to convert
            temp_input = input("Enter the temperature to convert (or type 'exit' to quit): ").strip()
            if temp_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            # Validate the input to ensure it is a numeric value
            if not temp_input.replace('.', '', 1).lstrip('-').isdigit():
                raise ValueError("Invalid temperature. Please enter a numeric value.")

            temp = float(temp_input)
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            # Perform the appropriate conversion
            if unit == 'F':
                converted_temp = convert_to_celsius(temp)
                print(f"{temp:.2f}F is {converted_temp:.2f}C.")
            elif unit == 'C':
                converted_temp = convert_to_fahrenheit(temp)
                print(f"{temp:.2f}C is {converted_temp:.2f}F.")
            else:
                raise ValueError("Invalid unit. Please specify 'C' for Celsius or 'F' for Fahrenheit.")

        except ValueError as e:
            # Handle invalid inputs
            print(e)
        except Exception as e:
            # Handle unexpected errors
            print(f"An unexpected error occurred: {e}")
        finally:
            # Notify the user the loop is still active
            print("---")

if __name__ == "__main__":
    main()