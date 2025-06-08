# shopping_list_manager.py

def display_menu():
    #Displays the main menu options to the user.
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    #Main function to run the shopping list manager.
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item.strip().capitalize()) 
            print(f"'{item.strip().capitalize()}' added to the list.")
        elif choice == '2':
            if not shopping_list:
                print("The list is empty. Nothing to remove.")
                continue
            
            item = input("Enter the item to remove: ")
            
            # Check if item exists (case-insensitive for better user experience)
           
            if item.strip().capitalize() in shopping_list:
                shopping_list.remove(item.strip().capitalize())
                print(f"'{item.strip().capitalize()}' removed from the list.")
            else:
                print(f"'{item.strip().capitalize()}' not found in the list.")
       
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("--------------------------")
        
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()