# Prompt the user to enter a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print '*' for each column in the row
    for col in range(size):
        print("*", end="")  # print '*' without moving to the next line
    
    # Print a newline after each row
    print()
    
    # Increment the row counter
    row += 1
