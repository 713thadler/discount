from utils import return_to_main_menu

# This function creates new employee records
def create_employee(employees):
    while True:
        employee_id = input("Enter Employee ID or 'M' to return to the main menu: ")
        if employee_id.upper() == 'M':
            return  # Return to main menu
        if not employee_id.isdigit() or any(emp[0] == int(employee_id) for emp in employees):
            print("Invalid input or Employee ID already exists. Please try again.")
            continue
        
        name = input("Enter Employee Name: ").strip()
        if not name:
            print("Employee name cannot be empty. Please try again.")
            continue
        
        emp_type = input("Enter Employee Type ('manager' or 'hourly'): ").lower()
        if emp_type not in ['manager', 'hourly']:
            print("Invalid employee type. Please enter 'manager' or 'hourly'.")
            continue
        
        years_worked = input("Enter Years Worked: ")
        if not years_worked.isdigit():
            print("Invalid input. Years Worked must be a number.")
            continue
        
        discount_number = int(employee_id) + 10000  # Simple unique discount number generation
        if any(emp[6] == discount_number for emp in employees):
            print("Error generating unique discount number. Please try again.")
            continue
        
        employees.append([int(employee_id), name, emp_type, int(years_worked), 0, 0, discount_number])
        print(f"Employee {name} added successfully.")
        
        if input("Add another employee? (yes/no): ").lower() != 'yes':
            break  # Stop adding employees if user input is not 'yes'

# This function displays the list of employees in a formatted or simple way
def display_employees(employees):
    print("\nDisplay Format Options:")
    print("1 - Print with format")
    print("2 - Simple print")
    format_choice = input("Choose the display format (1/2): ")

    if format_choice == '1':
        print("\nEmployee ID | Employee Name       | Employee Type | Years Worked | Total Purchased | Total Discount | Employee Discount Number")
        print("-" * 95)
        for emp in employees:
            print(f"{emp[0]:<11} | {emp[1]:<20} | {emp[2]:<13} | {emp[3]:<12} | ${emp[4]:<14} | ${emp[5]:<13} | {emp[6]}")
    elif format_choice == '2':
        for emp in employees:
            print(", ".join([str(emp[0]), emp[1], emp[2], str(emp[3]), f"${emp[4]}", f"${emp[5]}", str(emp[6])]))
    else:
        print("Invalid choice. Please select a valid format option.")

    # After displaying, check if user wants to return to the main menu
    if return_to_main_menu():
        return  # Return to main menu

