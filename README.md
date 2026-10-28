# ☕ Cafe Byte — Café Order Management System

**A Python-based café management application for processing customer orders, calculating bills, and analyzing sales performance.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-Portfolio-purple)
![Status](https://img.shields.io/badge/Status-Learning%20Project-orange)

## 📌 Overview

Cafe Byte is a command-line application developed in Python to simplify common café operations. It allows users to view menu items, place customer orders, calculate discounts and sales tax, generate receipts, and produce sales reports.

The project demonstrates practical Python programming concepts, including functions, dictionaries, tuples, loops, exception handling, file handling, variable-length arguments, and data analysis.

## ✨ Features

- **📋 Menu Management:** Load menu items, categories, and prices from a text file.
- **🛒 Order Processing:** Select menu items and quantities with input validation.
- **💰 Automated Billing:** Calculate subtotals, applicable discounts, sales tax, and final bills.
- **🎓 Student Discounts:** Apply additional discounts for customers with a student card.
- **🧾 Receipt Generation:** Display order details, subtotal, discount, tax, and total.
- **💵 Change Calculation:** Calculate the change due and break it down into available denominations.
- **📊 Sales Analysis:** Calculate order counts, revenue, quantities sold, and category-wise revenue.
- **🏆 Best-Selling Item:** Identify the item with the highest recorded quantity sold.
- **📈 Sales Recommendations:** Suggest promoting an item that has not been ordered or highlighting the best seller.
- **💾 File-Based Storage:** Save sales records and generate a daily report in text files.
- **🛡️ Input Validation:** Handle invalid menu choices, incorrect quantities, and invalid payment inputs.

## 🧮 Billing Rules

Cafe Byte uses the following discount structure:

| Order Subtotal | Discount |
|---|---:|
| Below Rs. 500 | 0% |
| Rs. 500–999 | 5% |
| Rs. 1,000 or above | 10% |
| Valid student card | Additional 5 percentage points |

**Sales tax:** 5% of the subtotal after discount.

The final bill is calculated using the subtotal, applicable discount, and sales tax.

## 🛠️ Tech Stack

- **Language:** Python 3
- **Data Structures:** Dictionaries, lists, tuples, and sets
- **Concepts:** Functions, loops, conditionals, variable scope, and exception handling
- **File Handling:** Text files for menu data, sales records, and reports
- **Interface:** Command-line interface (CLI)

## 📂 Project Structure

```text
cafe-byte/
│
├── cafebyte.py       # Main application
├── menu.txt          # Menu items, categories, and prices
├── sales.txt         # Recorded sales data (generated)
├── daily_report.txt  # Generated sales report
├── README.md         # Project documentation
└── .gitignore        # Git exclusion rules
```

*Note: `sales.txt` and `daily_report.txt` are created or updated by the application. The menu file must be prepared before running the program.*

## 🚀 Getting Started

### Prerequisites

- Python 3 installed on your computer
- A terminal or command prompt
- A text editor or Python IDE

### 1. Clone the Repository

```bash
git clone https://github.com/umairshabbirr/cafe-byte.git
```

### 2. Navigate to the Project Directory

```bash
cd cafe-byte
```

### 3. Prepare the Menu File

Create a file named `menu.txt` in the project directory.

Each line should contain the item name, category, and price, separated by commas.

Example:

```text
Tea,Drinks,100
Coffee,Drinks,200
Sandwich,Snacks,250
Burger,Meals,450
```

Use the supported categories: `Drinks`, `Snacks`, and `Meals`.

### 4. Run the Application

```bash
python cafebyte.py
```

If your system uses the `python3` command, run:

```bash
python3 cafebyte.py
```

## 🖥️ How to Use

After starting the application, select an option from the main menu:

```text
1. Show Menu
2. Place Order
3. Daily Report
4. Exit
```

- **Show Menu:** Display available items and their prices by category.
- **Place Order:** Enter item names and quantities, calculate the bill, and record the sale.
- **Daily Report:** Generate a report containing sales statistics and recommendations.
- **Exit:** Close the application.

Follow the on-screen prompts to complete each operation.

## 📊 Sales Reporting

The reporting module analyzes the records stored in `sales.txt` and generates `daily_report.txt`.

The report includes:

- Number of recorded orders
- Total recorded item revenue
- Quantities sold for each item
- Best-selling item
- Revenue by menu category
- Items that have not been ordered
- A promotional recommendation

**Data note:** The current implementation reads accumulated records from `sales.txt`; it does not automatically filter records by calendar date. The report reflects the sales data currently stored in that file.

## 🎯 Learning Objectives

This project was developed to practice and strengthen the following programming skills:

- Writing reusable functions
- Working with positional and keyword arguments
- Using `*args` and `**kwargs`
- Managing program state with global variables
- Reading and writing structured text files
- Validating user input with `try` and `except`
- Applying dictionaries and sets to sales analysis
- Implementing conditional business rules
- Generating reports from stored data

## 🔮 Future Improvements

Potential enhancements for future versions include:

- Integrating a database such as SQLite
- Adding a graphical user interface
- Supporting multiple orders and itemized digital receipts
- Introducing date-based sales tracking and historical reports
- Adding inventory and stock management
- Exporting sales reports to CSV or Excel
- Adding automated unit tests
- Improving monetary calculations and payment precision

## 👨‍💻 Author

**Umair**

Aspiring AI Engineer | BS Artificial Intelligence Student

GitHub: Umairshabbirr(https://github.com/umairshabbirr)

---

⭐ If you find this project useful for learning Python or understanding basic order-management systems, consider giving the repository a star.

*Built as a practical project to strengthen Python programming, problem-solving, and software development skills.*
