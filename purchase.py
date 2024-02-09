from lists import employees, items

def make_purchase(items, employees):
    def display_items():
        print("\nAvailable Items:")
        print("{:<12} | {:<25} | {:<12}".format("Item Number", "Item Name", "Original Price"))
        for item in items:
            print("{:<12} | {:<25} | ${:<10.2f}".format(item[0], item[1], item[2]))

    def calculate_discounted_price(employee, item_cost):
        years_worked = employee[3]
        role = employee[2].lower()
        discount_rate = min(2 * years_worked, 10) + (10 if role == 'manager' else 2 if role == 'hourly' else 0)
        discount_amount = (discount_rate / 100) * item_cost
        remaining_discount = 200 - employee[5]
        discount_amount = min(discount_amount, max(0, remaining_discount))
        return item_cost - discount_amount, discount_amount

    def get_employee_by_discount_number(discount_number):
        for employee in employees:
            if employee[-1] == discount_number:
                return employee
        return None

    def update_employee_discount_used(employee, discount_used):
        employee[5] += discount_used

    discount_number_input = input("Enter your Employee Discount Number to start purchasing, or 'NO' to exit: ")
    if discount_number_input.upper() == 'NO':
        return

    try:
        discount_number = int(discount_number_input)
        employee = get_employee_by_discount_number(discount_number)
        if not employee:
            print("Employee not found with the given discount number. Please try again.")
            return
    except ValueError:
        print("Invalid discount number. Please enter a numeric value.")
        return

    cart = []

    while True:
        if employee[5] >= 200:
            print("You have already used your $200 discount.")
            break

        display_items()
        item_num = input("Enter the Item Number to add to cart or 'DONE' to finish: ").strip()

        if item_num.upper() == 'DONE':
            break

        try:
            item_num = int(item_num)
            item = next((item for item in items if item[0] == item_num), None)
            if not item:
                print("Item not found. Please enter a valid item number.")
                continue
        except ValueError:
            print("Invalid item number. Please enter a numeric value.")
            continue

        discounted_price, discount_received = calculate_discounted_price(employee, item[2])
        if employee[5] + discount_received > 200:
            print("Adding this item would exceed your $200 discount limit. This item will not be added.")
            continue

        if discount_received > 0:
            update_employee_discount_used(employee, discount_received)
        cart.append((item[1], item[2], discounted_price, discount_received))
        print(f"Added {item[1]} to cart. Discounted price: ${discounted_price:.2f}. You saved: ${discount_received:.2f} on this item.")

    if cart:
        print("\nPurchase Receipt:")
        print("Employee Name:", employee[1])
        print("{:<25} | {:<15} | {:<18} | {:<15}".format("Item Name", "Original Price", "Discounted Price", "Amount Saved"))
        total_cost = 0
        total_saved = 0
        for item_name, orig_price, discounted_price, saved in cart:
            print("{:<25} | ${:<14} | ${:<17} | ${:<14}".format(item_name, orig_price, discounted_price, saved))
            total_cost += discounted_price
            total_saved += saved
        print(f"Total Original Price: ${sum(item[1] for item in cart):.2f}")
        print(f"Total Discounted Price: ${total_cost:.2f}")
        print(f"Total Saved: ${total_saved:.2f}")
    else:
        print("No items were added to the cart.")
