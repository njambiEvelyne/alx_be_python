# Define global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Global factor to convert Celsius to Fahrenheit
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Global factor to convert Fahrenheit to Celsius

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
            
            # Exit condition
            if temp_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            # Validate the input to ensure it is a numeric value
            try:
                temp = float(temp_input)
            except ValueError:
                raise ValueError("Invalid temperature. Please enter a numeric value.")

            # Prompt for the unit (Celsius or Fahrenheit)
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            if unit == 'F':
                # Fahrenheit to Celsius conversion with 14 decimal places
                converted_temp = convert_to_celsius(temp)
                print(f"{temp:.1f}°F is {converted_temp:.14f}°C.")  # 14 decimal places
            elif unit == 'C':
                # Celsius to Fahrenheit conversion with 1 decimal place
                converted_temp = convert_to_fahrenheit(temp)
                print(f"{temp:.1f}°C is {converted_temp:.1f}°F.")  # 1 decimal place
            else:
                raise ValueError("Invalid unit. Please specify 'C' for Celsius or 'F' for Fahrenheit.")

        except ValueError as e:
            # Handle invalid inputs with the specified message
            print(f"Error: {e}")
        except Exception as e:
            # Handle unexpected errors
            print(f"An unexpected error occurred: {e}")
        finally:
            # Notify the user the loop is still active
            print("---")

# Entry point of the script
if __name__ == "__main__":
    main()
