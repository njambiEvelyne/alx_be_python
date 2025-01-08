# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main program
def main()4
    :
    print("Temperature Conversion Tool")
    while True:
        try:
            # Get user input for temperature
            temp_input = input("Enter the temperature to convert (or type 'exit' to quit): ").strip()
            if temp_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break

            if not temp_input.replace('.', '', 1).lstrip('-').isdigit():
                print("Invalid input. Please enter a numeric value.")
                continue

            temp = float(temp_input)
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'F':
                converted_temp = convert_to_celsius(temp)
                print(f"{temp}F is {converted_temp:.2f}C.")
            elif unit == 'C':
                converted_temp = convert_to_fahrenheit(temp)
                print(f"{temp}C is {converted_temp:.2f}F.")
            else:
                print("Invalid unit. Please specify 'C' for Celsius or 'F' for Fahrenheit.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
