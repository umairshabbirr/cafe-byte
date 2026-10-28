# Café settings

# Display name of the café shown in welcome messages
CAFE_NAME = "Cafe Byte"
# Sales tax rate applied to order totals (5%)
TAX_RATE = 0.05
# Menu categories; a tuple because categories never change
CATEGORIES = ("Drinks", "Snacks", "Meals")
# Global counter for how many orders have been placed today
order_count = 0

print(f"Welcome to {CAFE_NAME}!")
print(type(CAFE_NAME))
print(type(TAX_RATE))
print(type(CATEGORIES))
print(type(order_count))


# Task 2
def give_change(paid, bill):
    change = paid - bill
    print(f"Change to return: Rs. {change}")

    hundreds = change // 100
    change = change % 100

    fifties = change // 50
    change = change % 50

    tens = change // 10
    change = change % 10

    fives = change // 5
    change = change % 5

    print(f"Rs. 100 x {hundreds}")
    print(f"Rs. 50 x {fifties}")
    print(f"Rs. 10 x {tens}")
    print(f"Rs. 5 x {fives}")


# Task 3: Read the menu file
def load_menu(filename):
    prices = {}
    category_of = {}
    try:
        with open(filename) as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                item, category, price = line.split(",")
                item = item.strip()
                category = category.strip()
                price = int(price.strip())
                prices[item] = price
                category_of[item] = category
    except FileNotFoundError:
        print("Error: menu file not found!")
        return {}, {}
    return prices, category_of


# Task 4: Show the menu
def show_menu(prices, category_of):
    for category in CATEGORIES:
        print(f"\n--- {category} ---")
        for item in category_of:
            if category_of[item] == category:
                print(f"{item}: Rs. {prices[item]}")


# Task 5: Subtotal
def calculate_subtotal(*amounts):
    total = 0
    for amount in amounts:
        total = total + amount
    return total


# Task 6: Discount rule
def get_discount_rate(subtotal, student=False):
    if subtotal >= 1000:
        rate = 0.10
    elif subtotal >= 500:
        rate = 0.05
    else:
        rate = 0.0

    if student:
        rate = rate + 0.05

    return rate


# Task 7: Final bill
def final_bill(subtotal, student=False):
    rate = get_discount_rate(subtotal, student)
    discount = subtotal * rate
    tax = (subtotal - discount) * TAX_RATE
    total = round(subtotal - discount + tax, 2)
    return discount, tax, total


# Task 8: Receipt
def print_receipt(**details):
    print("=" * 30)
    for key, value in details.items():
        print(f"{key}: {value}")
    print("=" * 30)


# Task 9: Place an order
def place_order(prices):
    global order_count
    order = []
    while True:
        item = input("Item name (or done): ").strip().title()
        if item == "Done":
            break
        if item not in prices:
            print(f"Sorry, {item} is not on the menu.")
            continue
        while True:
            try:
                qty = int(input("Quantity: "))
                if qty >= 1:
                    break
                print("Quantity must be at least 1.")
            except ValueError:
                print("Please enter a number for the quantity, not letters.")
        order.append((item, qty))

    if len(order) == 0:
        return order

    # Task 10: Bill the order
    order_count = order_count + 1

    amounts = []
    for item, qty in order:
        amounts.append(prices[item] * qty)
    subtotal = calculate_subtotal(*amounts)

    student_answer = input("Student card? (y/n): ").strip().lower()
    student = student_answer == "y"

    discount, tax, total = final_bill(subtotal, student)
    print_receipt(
        Order=order_count,
        Subtotal=subtotal,
        Discount=discount,
        Tax=tax,
        Total=total,
    )

    bill = int(round(total))
    while True:
        try:
            paid = int(input("Amount paid (Rs.): "))
            if paid < bill:
                print(f"That is not enough. The bill is Rs. {bill}.")
                continue
            break
        except ValueError:
            print("Please enter a number for the amount paid, not letters.")
    give_change(paid, bill)

    # Task 11: Save to file
    with open("sales.txt", "a") as file:
        for item, qty in order:
            amount = prices[item] * qty
            file.write(f"{order_count},{item},{qty},{amount}\n")

    return order


# Task 12: Analyse the sales
def daily_report(prices, category_of):
    try:
        with open("sales.txt") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No sales yet today.")
        return

    order_numbers = set()
    revenue = 0
    items_sold = {}
    category_revenue = {category: 0 for category in CATEGORIES}

    for line in lines:
        line = line.strip()
        if not line:
            continue
        order_number, item, quantity, amount = line.split(",")
        order_numbers.add(order_number)
        quantity = int(quantity)
        amount = int(amount)
        revenue = revenue + amount
        if item in items_sold:
            items_sold[item] = items_sold[item] + quantity
        else:
            items_sold[item] = quantity
        category = category_of.get(item)
        if category in category_revenue:
            category_revenue[category] = category_revenue[category] + amount

    if len(items_sold) == 0:
        print("No sales yet today.")
        return

    best_seller = None
    best_qty = 0
    for item in items_sold:
        if items_sold[item] > best_qty:
            best_qty = items_sold[item]
            best_seller = item

    not_ordered = set(prices.keys()) - set(items_sold.keys())

    if not_ordered:
        promote = sorted(not_ordered)[0]
        recommendation = (
            f"Promote {promote} - it was not ordered today and needs a boost."
        )
    else:
        recommendation = f"Promote {best_seller} as today's special!"

    report_lines = [
        f"Orders today: {len(order_numbers)}",
        f"Revenue: {revenue}",
        f"Items sold: {items_sold}",
        f"Best seller: {best_seller}",
        f"Category revenue: {category_revenue}",
        f"Not ordered today: {sorted(not_ordered)}",
        f"Recommendation: {recommendation}",
    ]

    with open("daily_report.txt", "w") as file:
        for line in report_lines:
            print(line)
            file.write(line + "\n")


# Main program
prices, category_of = load_menu("menu.txt")

menu_options = {
    1: "Show Menu",
    2: "Place Order",
    3: "Daily Report",
    4: "Exit",
}

while True:
    print("\n1. Show Menu  2. Place Order  3. Daily Report  4. Exit")
    try:
        choice = int(input("Enter choice: ").strip())
    except ValueError:
        print("Please enter a number for the menu choice, not letters.")
        continue

    option = menu_options.get(choice, "Invalid")

    if option == "Show Menu":
        show_menu(prices, category_of)
    elif option == "Place Order":
        place_order(prices)
    elif option == "Daily Report":
        daily_report(prices, category_of)
    elif option == "Exit":
        print(f"Thank you for visiting {CAFE_NAME}")
        break
    else:
        print("Invalid choice, try again.")
