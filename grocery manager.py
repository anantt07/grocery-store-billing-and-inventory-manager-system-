# grocery store billing and inventory manager system 
import json
import os
from datetime import datetime

file_name = "inventory.json"
gst = 5
low_stock = 10

store = {}


# load data from the file
def load_data():
    global store

    if os.path.exists(file_name):
        f = open(file_name, "r")
        store = json.load(f)
        f.close()
    else:
        # some items for the first time
        store = {
            "101": {"name": "Rice 1kg", "price": 60, "qty": 50},
            "102": {"name": "Sugar 1kg", "price": 45, "qty": 40},
            "103": {"name": "Milk 1L", "price": 30, "qty": 25},
            "104": {"name": "Bread", "price": 25, "qty": 8},
            "105": {"name": "Eggs (12)", "price": 84, "qty": 30}
        }

        save_data()


# save current data
def save_data():
    f = open(file_name, "w")
    json.dump(store, f, indent=4)
    f.close()


def display():
    print("\n----- INVENTORY -----")

    if len(store) == 0:
        print("No items in the store.")
        return

    for code in store:
        item = store[code]

        print(
            code,
            "-", item["name"],
            "| Price:", item["price"],
            "| Quantity:", item["qty"]
        )


def add():
    print("\n--- ADD ITEM ---")

    code = input("Enter item code: ")

    if code in store:
        print("This code already exists.")
        return

    name = input("Enter item name: ")

    try:
        price = float(input("Enter price: "))
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter numbers only.")
        return

    if price <= 0:
        print("Price must be greater than 0.")
        return

    if qty < 0:
        print("Quantity cannot be negative.")
        return

    store[code] = {
        "name": name,
        "price": price,
        "qty": qty
    }

    save_data()
    print("Item added.")


def stock():
    print("\n--- UPDATE STOCK ---")

    code = input("Enter item code: ")

    if code not in store:
        print("Item not found.")
        return

    print("Current stock:", store[code]["qty"])

    try:
        change = int(input("Enter quantity to add/remove: "))
    except ValueError:
        print("Enter a whole number.")
        return

    new_stock = store[code]["qty"] + change

    if new_stock < 0:
        print("Stock cannot be negative.")
        return

    store[code]["qty"] = new_stock

    save_data()

    print("Stock updated.")
    print("New stock:", new_stock)


def change_price():
    print("\n--- CHANGE PRICE ---")

    code = input("Enter item code: ")

    if code not in store:
        print("Item not found.")
        return

    try:
        price = float(input("Enter new price: "))
    except ValueError:
        print("Please enter a valid price.")
        return

    if price <= 0:
        print("Price must be greater than 0.")
        return

    store[code]["price"] = price

    save_data()

    print("Price updated.")


def remove():
    print("\n--- DELETE ITEM ---")

    code = input("Enter item code: ")

    if code not in store:
        print("Item not found.")
        return

    print("Item:", store[code]["name"])

    answer = input("Delete this item? (y/n): ")

    if answer.lower() == "y":
        del store[code]
        save_data()
        print("Item deleted.")
    else:
        print("Item was not deleted.")


def check_stock():
    print("\n--- LOW STOCK ---")

    found = False

    for code in store:
        item = store[code]

        if item["qty"] <= low_stock:
            print(
                item["name"],
                "- code:", code,
                "- only", item["qty"], "left"
            )
            found = True

    if found == False:
        print("No low stock items.")


def bill():
    print("\n--- NEW BILL ---")

    customer = input("Customer name: ")

    if customer == "":
        customer = "Customer"

    cart = []

    while True:
        code = input("Enter item code (or done): ")

        if code.lower() == "done":
            break

        if code not in store:
            print("Item not found.")
            continue

        item = store[code]

        try:
            qty = int(input("Enter quantity: "))
        except ValueError:
            print("Enter a number.")
            continue

        if qty <= 0:
            print("Quantity must be greater than 0.")
            continue

        # check if the same item is already in the cart
        already = 0

        for x in cart:
            if x["code"] == code:
                already = already + x["qty"]

        if already + qty > item["qty"]:
            print("Not enough stock.")
            print("Available:", item["qty"])
            continue

        cart.append({
            "code": code,
            "name": item["name"],
            "price": item["price"],
            "qty": qty
        })

        print(item["name"], "added.")

    if len(cart) == 0:
        print("No items added.")
        return

    # calculate bill
    subtotal = 0

    for item in cart:
        amount = item["price"] * item["qty"]
        subtotal = subtotal + amount

    tax = subtotal * gst / 100
    total = subtotal + tax

    print("\n==============================")
    print("        GROCERY STORE")
    print("==============================")

    date = datetime.now().strftime("%d-%m-%Y %H:%M")

    print("Date:", date)
    print("Customer:", customer)
    print("------------------------------")

    for item in cart:
        amount = item["price"] * item["qty"]

        print(
            item["name"],
            "-", item["qty"],
            "x", item["price"],
            "=", amount
        )

    print("------------------------------")
    print("Subtotal:", round(subtotal, 2))
    print("GST:", round(tax, 2))
    print("Total:", round(total, 2))
    print("==============================")
    print("Thank you! Visit again.")

    # reduce stock after the sale
    for item in cart:
        code = item["code"]
        store[code]["qty"] = store[code]["qty"] - item["qty"]

    save_data()


def main():
    load_data()

    while True:
        print("\n===== GROCERY STORE =====")
        print("1. Show inventory")
        print("2. Add item")
        print("3. Update stock")
        print("4. Change price")
        print("5. Delete item")
        print("6. Low stock report")
        print("7. Make bill")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display()

        elif choice == "2":
            add()

        elif choice == "3":
            stock()

        elif choice == "4":
            change_price()

        elif choice == "5":
            remove()

        elif choice == "6":
            check_stock()

        elif choice == "7":
            bill()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()
