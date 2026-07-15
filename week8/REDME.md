# Food Delivery Receipt Generator

## Overview

This project is a simple Python application that generates a receipt for a food delivery order. The program is divided into separate modules to follow good programming practices.

---

## Project Structure

```
week_8/
│── main.py
│── customer.py
│── receipt.py
└── README.md
```

---

## Modules

### 1. `main.py`
- Imports the required modules.
- Calls the customer module to collect customer information.
- Calls the receipt module to display the receipt.

### 2. `customer.py`
- Collects customer information:
  - Customer name
  - Food ordered
  - Quantity
  - Price per item
  - Delivery option (Y/N)
- Calculates the delivery charge.
- Returns all data to the main program.

### 3. `receipt.py`
- Calculates:
  - Subtotal
  - Service charge (5%)
  - Grand total
- Prints the formatted receipt.

---

## Features

- Customer information input
- Food order processing
- Automatic subtotal calculation
- 5% service charge calculation
- Optional delivery charge
- Receipt generation

---

## Formula

```
Subtotal = Quantity × Price

Service Charge = Subtotal × 5%

Grand Total = Subtotal + Service Charge + Delivery Charge
```

---

## How to Run

1. Open the project folder.
2. Open the terminal.
3. Run the following command:

```bash
python main.py
```

---

## Example Output

```
=== Customer Information ===

Customer Name : izzad
Food Ordered (Cake/Muffin): Cake
Quantity : 2
Price per Item (RM): 3
Delivery (Y/N): Y

========== RECEIPT ==========
Customer : izzad
Food     : Cake
Quantity : 2
Price    : RM 3.00
------------------------------
Subtotal : RM 6.00
Service Charge (5%) : RM 0.30
Delivery Charge : RM 5.00
------------------------------
TOTAL : RM 11.30
==============================
```

---

## Author

**Name:** Your Name

**Course:** Software Engineering

**Week:** Tutorial 8