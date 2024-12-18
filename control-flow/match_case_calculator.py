# Prompt the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user for the operation type
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using a match case statement
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            result = "Cannot divide by zero."
        else:
            result = num1 / num2
    case _:
        result = "Invalid operation."

# Output the result
print(f"The result is {result}")
