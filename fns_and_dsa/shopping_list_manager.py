def display_menu():  
    """Display the menu options for the shopping list manager."""  
    print(f"\nShopping List Manager")  
    print("1. Add Item")  
    print("2. Remove Item")  
    print("3. View List")  
    print("4. Exit")  

def main():  
    shopping_list = []  # Start with an empty shopping list  
    
    while True:  
        display_menu()  # Call the function to display the menu  
        choice = input("Enter your choice: ")  

        if choice == '1':  
            # Prompt for and add an item  
            item = input("Enter the item name to add: ")  
            shopping_list.append(item)  # Append the item to the shopping list  
            print(f"{item} has been added to the shopping list.")  
        elif choice == '2':  
            # Prompt for and remove an item  
            item = input("Enter the item name to remove: ")  
            if item in shopping_list:  
                shopping_list.remove(item)  # Remove the item from the shopping list  
                print(f"{item} has been removed from the shopping list.")  
            else:  
                print(f"{item} not found in the shopping list.")  
        elif choice == '3':  
            # Display the shopping list  
            if shopping_list:  
                print("Current Shopping List:")  
                for index, item in enumerate(shopping_list, start=1):  
                    print(f"{index}. {item}")  # Print each item with its index  
            else:  
                print("The shopping list is currently empty.")  
        elif choice == '4':  
            print("Goodbye!")  # Exit message  
            break  
        else:  
            print("Invalid choice. Please try again.")  # Handle invalid choices  

if __name__ == "__main__":  
    main()  # Run the main function