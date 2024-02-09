
from utils import return_to_main_menu
from lists import employees
from employee_management import display_employees


def display_items_with_format_choice(items):
    while True:
        display_format = input("Choose display format 1 for formatted print, 2 for simple print, or 'M' to return to the main menu: ")
        if display_format == '1':
            print_formatted_items(items)
            return True
        elif display_format == '2':
            print_simple_items(items)
            return True
        elif display_format.upper() == 'M':
            return False
        else:
            print("Invalid choice, please try again.")

def print_formatted_items(items):
    header = "{:<12} | {:<20} | {:<10}"
    divider = "-" * 48
    print(header.format("Item Number", "Item Name", "Item Cost"))
    print(divider)
    for item in items:
        print("{:<12} | {:<20} | ${:<10.2f}".format(*item))

def print_simple_items(items):
    for item in items:
        print("{}, {}, ${:.2f}".format(*item))
