# Contains utility functions used throughout the application

def return_to_main_menu():
    choice = input("Press 'M' to return to the main menu or any other key to continue: ").upper()
    return choice == 'M'
