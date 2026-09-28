# Grocery Store Billing and Inventory Manager

## Project Description

The Grocery Store Billing and Inventory Manager is a simple Python-based program used to manage grocery store items, stock, prices, and customer bills.

The program stores inventory data in a JSON file so that the data is not lost when the program is closed. It provides a menu-driven interface through which the user can view items, add new items, update stock, change prices, delete items, check low-stock items, and create bills.

## Features

- Display all grocery items in the inventory.
- Add a new item with its code, name, price, and quantity.
- Update the stock quantity of an existing item.
- Increase or decrease stock.
- Change the price of an item.
- Delete an item from the inventory.
- Display items whose stock is low.
- Create a customer bill.
- Calculate subtotal, GST, and final total.
- Automatically reduce stock after a sale.
- Save inventory data in `inventory.json`.
- Load previously saved inventory data when the program starts.
- Validate basic user input such as invalid numbers and negative quantities.

## Technologies Used

- **Python**
- **JSON** for storing inventory data
- **OS module** for checking whether the inventory file exists
- **Datetime module** for displaying the date and time on bills

## Requirements

- Python 3.x
- No external Python libraries are required.

## How to Run

1. Save the Python program in a file, for example:

   `grocery_store.py`

2. Open a terminal or command prompt in the folder containing the file.

3. Run:

   ```bash
   python grocery_store.py
   ```

4. The program will display the main menu.

## Main Menu

```text
===== GROCERY STORE =====
1. Show inventory
2. Add item
3. Update stock
4. Change price
5. Delete item
6. Low stock report
7. Make bill
8. Exit
```

### 1. Show Inventory

Displays all items currently stored in the inventory along with:

- Item code
- Item name
- Price
- Quantity

### 2. Add Item

Allows the user to add a new grocery item by entering:

- Item code
- Item name
- Price
- Quantity

The program checks that the item code is not already being used and that the price and quantity are valid.

### 3. Update Stock

Allows the user to add or remove stock from an existing item.

For example, entering `10` adds 10 items, while entering `-5` removes 5 items.

The program does not allow the stock to become negative.

### 4. Change Price

Allows the user to enter a new price for an existing item.

### 5. Delete Item

Removes an item from the inventory after asking the user for confirmation.

### 6. Low Stock Report

Displays items whose quantity is less than or equal to the low-stock limit.

The current low-stock limit is:

```text
10 items
```

### 7. Make Bill

Creates a bill for a customer.

The user enters:

- Customer name
- Item code
- Quantity

The program checks whether enough stock is available before adding an item to the bill.

The bill contains:

- Date and time
- Customer name
- Items purchased
- Quantity
- Price
- Subtotal
- GST
- Final total

The GST used in the program is:

```text
5%
```

After the bill is completed, the purchased quantities are automatically removed from the inventory.

### 8. Exit

Closes the program.

## Data Storage

The inventory is stored in a file named:

```text
inventory.json
```

Example data structure:

```json
{
    "101": {
        "name": "Rice 1kg",
        "price": 60,
        "qty": 50
    }
}
```

If `inventory.json` does not exist when the program is started, the program creates an initial inventory containing sample grocery items.

## Initial Items

The first-time inventory contains:

| Code | Item | Price | Quantity |
|---|---|---:|---:|
| 101 | Rice 1kg | 60 | 50 |
| 102 | Sugar 1kg | 45 | 40 |
| 103 | Milk 1L | 30 | 25 |
| 104 | Bread | 25 | 8 |
| 105 | Eggs (12) | 84 | 30 |

## Program Structure

The program is divided into several functions:

- `load_data()` - Loads inventory from the JSON file.
- `save_data()` - Saves the current inventory.
- `display()` - Displays all inventory items.
- `add()` - Adds a new item.
- `stock()` - Updates item stock.
- `change_price()` - Changes an item's price.
- `remove()` - Deletes an item.
- `check_stock()` - Shows low-stock items.
- `bill()` - Creates a customer bill and updates stock.
- `main()` - Displays the main menu and controls the program.

## Validation

The program performs basic validation, including:

- Duplicate item codes are not allowed.
- Prices must be greater than zero.
- Quantities cannot be negative.
- Stock cannot become negative.
- Billing quantity must be greater than zero.
- A bill cannot be created without adding an item.
- The program checks available stock before making a sale.

## Future Improvements

Some possible improvements are:

- Add employee/user login.
- Store previous bills.
- Add customer phone numbers.
- Generate printable bills.
- Add sales reports.
- Add search functionality.
- Add categories for grocery items.
- Add discount functionality.
- Add monthly sales analysis.

## Conclusion

This project demonstrates how Python can be used to create a simple real-world grocery store management system. It uses basic Python concepts such as functions, dictionaries, lists, loops, conditional statements, exception handling, file handling, JSON, and date/time operations.
