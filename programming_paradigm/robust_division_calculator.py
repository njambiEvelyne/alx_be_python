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

        # Perform the division
        return f"The result of the division is {num / denom:.2f}"

    except ValueError:
        return "Error: Please enter numeric values only."
