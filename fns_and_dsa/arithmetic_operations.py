def perform_operation(num1, num2, operation):  
    """Perform basic arithmetic operations on two numbers."""  
    if operation == 'add':  
        return num1 + num2  
    elif operation == 'subtract':  
        return num1 - num2  
    elif operation == 'multiply':  
        return num1 * num2  
    elif operation == 'divide':  
        if num2 == 0:  
            return "Error: Division by zero is not allowed."  
        return num1 / num2  
    else:  
        return "Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."