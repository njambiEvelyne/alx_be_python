# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    """
    Command-line interface for the division calculator.
    """
    # Ensure exactly 2 arguments are provided (numerator and denominator)
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Extract numerator and denominator from command line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function and display the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
