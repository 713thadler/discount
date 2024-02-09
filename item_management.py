from utils import return_to_main_menu
from employee_management import display_employees
from lists import employees


def add_item(items):
    while True:
        print("\nAdding a new item.")
        item_input = input("Enter Item Number (numeric), 'NO' to finish, or 'M' to return to the main menu: ")

        if item_input.upper() == 'M':
            if return_to_main_menu():
                return
        elif item_input.upper() == 'NO':
            print("Finished adding items.")
            break

        if not item_input.isdigit():
            print("Invalid input. Please enter a numeric Item Number.")
            continue

        item_number = int(item_input)
        if any(item[0] == item_number for item in items):
            print("Error: Item Number already exists. Try again.")
            continue

        item_name = input("Enter Item Name: ").strip()
        if not item_name:
            print("Item name cannot be empty. Please try again.")
            continue

        item_cost_input = input("Enter Item Cost ($): ")
        try:
            item_cost = float(item_cost_input)
            if item_cost <= 0:
                raise ValueError("Item cost must be greater than 0.")
        except ValueError as e:
            print(f"Invalid input. {str(e)}")
            continue

        items.append([item_number, item_name, item_cost])
        print(f"Item '{item_name}' added successfully with a cost of ${item_cost:.2f}.")

        # Ask if the user wants to add another item
        if not ask_to_continue_adding():
            break

def ask_to_continue_adding():
    choice = input("Add another item? (YES/NO): ").upper()
    return choice == 'YES'

