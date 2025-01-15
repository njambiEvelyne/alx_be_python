# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform division with robust error handling.
    Arguments:
        numerator: The number to be divided.
        denominator: The number by which to divide.
    Returns:
        The result of the division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."

        # Perform the division and format the result to remove unnecessary trailing zeros
        result = num / denom
        return f"The result of the division is {result:.15g}"  # Use general formatting
    except ValueError:
        return "Error: Please enter numeric values only."
