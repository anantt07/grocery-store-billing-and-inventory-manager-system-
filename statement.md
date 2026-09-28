# Project Statement

## Project Title

**Grocery Store Billing and Inventory Manager**

## Problem Statement

Managing grocery store inventory and preparing customer bills manually can take time and may lead to mistakes in stock quantities, prices, and billing calculations.

The purpose of this project is to develop a simple Python-based Grocery Store Billing and Inventory Manager that helps a store manage its products and prepare customer bills.

The system should allow the store user to maintain item details such as item code, name, price, and quantity. It should also provide a way to update stock, change prices, remove items, identify low-stock products, and generate customer bills.

The inventory information should be saved in a JSON file so that it remains available even after the program is closed.

## Objectives

The main objectives of the project are:

1. To maintain grocery store inventory using Python.
2. To store product details such as code, name, price, and quantity.
3. To add and remove products from the inventory.
4. To update product stock.
5. To update product prices.
6. To identify products with low stock.
7. To create customer bills.
8. To calculate subtotal, GST, and final bill amount.
9. To automatically reduce inventory after a sale.
10. To store inventory information permanently using a JSON file.

## Scope of the Project

The project is designed for basic grocery store inventory and billing management.

The system covers:

- Product management
- Stock management
- Price management
- Low-stock checking
- Customer billing
- GST calculation
- File-based data storage

The project is intended as a simple command-line application and does not include an online payment system or a graphical user interface.

## Functional Requirements

### 1. Inventory Display

The system should display all available grocery items along with their:

- Item code
- Item name
- Price
- Quantity

### 2. Add Item

The system should allow the user to add a new item.

The user should enter:

- Item code
- Item name
- Price
- Quantity

The system should not allow duplicate item codes.

### 3. Stock Management

The system should allow the user to increase or decrease the stock of an existing item.

The stock quantity should never become negative.

### 4. Price Management

The system should allow the user to change the price of an existing item.

The new price must be greater than zero.

### 5. Delete Item

The system should allow the user to remove an existing item after confirmation.

### 6. Low Stock Report

The system should identify products whose quantity is at or below the low-stock limit.

The current low-stock limit is 10 items.

### 7. Billing

The system should allow the user to create a bill for a customer.

The user should be able to select items using their item codes and enter the required quantities.

The system should check the available stock before adding an item to the bill.

### 8. Bill Calculation

The system should calculate:

- Item amount
- Subtotal
- GST
- Final total

The GST rate used by the system is 5%.

The calculation is:

```text
Item Amount = Price × Quantity

Subtotal = Sum of all item amounts

GST = Subtotal × 5 / 100

Total = Subtotal + GST
```

### 9. Stock Update After Sale

After a successful bill is completed, the quantity of each purchased item should be reduced from the inventory.

### 10. Data Persistence

The system should save inventory information in `inventory.json`.

When the program starts, it should load the previously saved inventory if the file exists.

## Non-Functional Requirements

### Usability

The program should have a simple menu-based interface that is easy for a beginner to understand.

### Reliability

The program should validate user input and prevent invalid stock quantities and prices.

### Data Persistence

Inventory data should remain available after the program is closed by saving it to a JSON file.

### Maintainability

The program should use separate functions for different operations so that the code is easier to understand and modify.

## Input

The system accepts input such as:

- Item code
- Item name
- Item price
- Item quantity
- Customer name
- Menu choice
- Stock changes

## Output

The system produces:

- Inventory list
- Low-stock report
- Confirmation messages
- Customer bills
- Subtotal
- GST amount
- Final bill total

## Tools and Technologies

| Tool/Technology | Purpose |
|---|---|
| Python | Main programming language |
| JSON | Store inventory data |
| `os` | Check whether the inventory file exists |
| `datetime` | Display date and time on bills |

## Python Concepts Used

The project demonstrates the following Python concepts:

- Variables
- Dictionaries
- Lists
- Functions
- `if-elif-else`
- `for` loops
- `while` loops
- User input
- Exception handling
- File handling
- JSON
- Global variables
- Arithmetic operations
- String operations
- Date and time handling

## Expected Result

The completed system should provide a working command-line application through which a grocery store user can manage inventory and create customer bills.

The system should keep inventory data updated and automatically reduce stock whenever a sale is completed.

## Conclusion

The Grocery Store Billing and Inventory Manager provides a simple solution for handling common grocery store operations. The project combines inventory management, billing, GST calculation, and JSON-based file storage into one Python application.

It also provides practical use of fundamental Python programming concepts in a real-world problem.
