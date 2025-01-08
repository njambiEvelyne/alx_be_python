def display_menu():  
    """Display the menu options for the shopping list manager."""  
    print("\nShopping List Manager")  
    print("1. Add Item")  
    print("2. Remove Item")  
    print("3. View List")  
    print("4. Exit")  

def main():  
    shopping_list = []  # Implementation of an array (list) for storing shopping items  
    while True:  
        display_menu()  # Calling the display_menu function  
        choice = input("Enter your choice (1-4): ")  

        # Check if choice input is a number  
        if choice.isdigit() and int(choice) in range(1, 5):  
            choice = int(choice)  # Convert choice to an integer  

            if choice == 1:  
                # Prompt for and add an item  
                item = input("Enter the item name to add: ")  
                shopping_list.append(item)  
                print(f"{item} has been added to the shopping list.")  
            elif choice == 2:  
                # Prompt for and remove an item  
                item = input("Enter the item name to remove: ")  
                if item in shopping_list:  
                    shopping_list.remove(item)  
                    print(f"{item} has been removed from the shopping list.")  
                else:  
                    print(f"{item} not found in the shopping list.")  
            elif choice == 3:  
                # Display the shopping list  
                if shopping_list:  
                    print("Current Shopping List:")  
                    for index, item in enumerate(shopping_list, start=1):  
                        print(f"{index}. {item}")  
                else:  
                    print("The shopping list is currently empty.")  
            elif choice == 4:  
                print("Goodbye!")  
                break  
        else:  
            print("Invalid choice. Please enter a number between 1 and 4.")  

if __name__ == "__main__":  
    main()