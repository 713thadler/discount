from employee_management import create_employee, display_employees
from utils import return_to_main_menu
from lists import employees, items
from item_display import display_items_with_format_choice
from purchase import make_purchase
from item_management import add_item

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Add a new employee")
        print("2. Add a new item")
        print("3. Record a purchase")
        print("4. Show a summary of all employees")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        
        try:
            choice_int = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        match choice_int:
            case 1:
                create_employee(employees)
            case 2:
                add_item(items)
            case 3:
                make_purchase(items, employees)
            case 4:
                all_employees = input("Do you want to see all employees? (yes/no): ").lower()
                if all_employees not in ['yes', 'no']:
                    print("Invalid response. Please enter 'yes' or 'no'.")
                    continue
                if all_employees == 'yes':
                    display_employees(employees)
            case 5:
                print("Exiting the program.")
                break
            case _:
                print("Choice must be a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()
