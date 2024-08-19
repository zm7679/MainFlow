import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import ttk
import os
import tkinter as tk
from tkinter import messagebox

# Function to create the necessary tables
import sqlite3

# Function to create the necessary tables
def create_tables():
    conn = sqlite3.connect('billing.db')
    c = conn.cursor()

    # Drop the tables if they exist (for debugging or resetting)
    c.execute("DROP TABLE IF EXISTS customers")
    c.execute("DROP TABLE IF EXISTS products")
    c.execute("DROP TABLE IF EXISTS transactions")

    # Create customers table
    c.execute('''CREATE TABLE customers
                 (CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
                  CustomerName TEXT NOT NULL,
                  Phone TEXT,
                  Email TEXT)''')

    # Create products table
    c.execute('''CREATE TABLE products
                 (ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
                  ProductName TEXT NOT NULL,
                  Price REAL NOT NULL,
                  Quantity INTEGER NOT NULL)''')

    # Create transactions table
    c.execute('''CREATE TABLE transactions
                 (TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
                  CustomerID INTEGER,
                  ProductID INTEGER,
                  Quantity INTEGER NOT NULL,
                  TotalAmount REAL NOT NULL,
                  Date TEXT NOT NULL,
                  FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID),
                  FOREIGN KEY (ProductID) REFERENCES products(ProductID))''')

    conn.commit()
    conn.close()

# Call the function to create the tables
create_tables()


# The rest of the script should follow as previously provided


# Function to add product to the database
def add_product():
    name = product_name_entry.get()
    price = float(price_entry.get())
    quantity = int(quantity_entry.get())
    conn = sqlite3.connect('billing.db')
    c = conn.cursor()
    c.execute("INSERT INTO products (ProductName, Price, Quantity) VALUES (?, ?, ?)",
              (name, price, quantity))
    conn.commit()
    conn.close()
    product_name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Product added successfully!")
    update_product_menu()

# Function to add customer to the database
def add_customer():
    name = customer_name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    conn = sqlite3.connect('billing.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers (CustomerName, Phone, Email) VALUES (?, ?, ?)",
              (name, phone, email))
    conn.commit()
    conn.close()
    customer_name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Customer added successfully!")

# Function to add selected product to the bill
def add_to_bill():
    product = product_dropdown.get()
    quantity = int(billing_quantity_entry.get())
    conn = sqlite3.connect('billing.db')
    c = conn.cursor()
    c.execute("SELECT Price FROM products WHERE ProductName=?", (product,))
    price = c.fetchone()[0]
    total = price * quantity
    bill_tree.insert("", "end", values=(product, quantity, f"${total:.2f}"))
    conn.close()
    calculate_total()

# Function to calculate total amount
def calculate_total():
    total = 0
    for child in bill_tree.get_children():
        total += float(bill_tree.item(child, 'values')[2].replace('$', ''))
    total_amount_label.config(text=f"${total:.2f}")

# Function to generate invoice
def generate_invoice():
    messagebox.showinfo("Invoice", "Invoice generated successfully!")

# Function to update product menu after adding a new product
def update_product_menu():
    conn = sqlite3.connect('billing.db')
    c = conn.cursor()
    c.execute("SELECT ProductName FROM products")
    products = [row[0] for row in c.fetchall()]
    conn.close()
    product_menu['values'] = products

# GUI setup
root = tk.Tk()
root.title("Billing Software")

# Product Entry Frame
product_frame = tk.Frame(root)
product_frame.pack(pady=10)
tk.Label(product_frame, text="Product Name").grid(row=0, column=0)
tk.Label(product_frame, text="Price").grid(row=1, column=0)
tk.Label(product_frame, text="Quantity").grid(row=2, column=0)
product_name_entry = tk.Entry(product_frame)
product_name_entry.grid(row=0, column=1)
price_entry = tk.Entry(product_frame)
price_entry.grid(row=1, column=1)
quantity_entry = tk.Entry(product_frame)
quantity_entry.grid(row=2, column=1)
tk.Button(product_frame, text="Add Product", command=add_product).grid(row=3, column=1)

# Customer Entry Frame
customer_frame = tk.Frame(root)
customer_frame.pack(pady=10)
tk.Label(customer_frame, text="Customer Name").grid(row=0, column=0)
tk.Label(customer_frame, text="Phone").grid(row=1, column=0)
tk.Label(customer_frame, text="Email").grid(row=2, column=0)
customer_name_entry = tk.Entry(customer_frame)
customer_name_entry.grid(row=0, column=1)
phone_entry = tk.Entry(customer_frame)
phone_entry.grid(row=1, column=1)
email_entry = tk.Entry(customer_frame)
email_entry.grid(row=2, column=1)
tk.Button(customer_frame, text="Add Customer", command=add_customer).grid(row=3, column=1)

# Billing Frame
billing_frame = tk.Frame(root)
billing_frame.pack(pady=10)
tk.Label(billing_frame, text="Select Product").grid(row=0, column=0)

# Fetch products from the database for the dropdown
conn = sqlite3.connect('billing.db')
c = conn.cursor()
c.execute("SELECT ProductName FROM products")
products = [row[0] for row in c.fetchall()]
conn.close()

product_dropdown = tk.StringVar()
product_menu = ttk.Combobox(billing_frame, textvariable=product_dropdown, values=products)
product_menu.grid(row=0, column=1)
tk.Label(billing_frame, text="Quantity").grid(row=1, column=0)
billing_quantity_entry = tk.Entry(billing_frame)
billing_quantity_entry.grid(row=1, column=1)
tk.Button(billing_frame, text="Add to Bill", command=add_to_bill).grid(row=2, column=1)

# Bill Treeview (for displaying the bill)
bill_tree = ttk.Treeview(root, columns=("Product", "Quantity", "Total"), show="headings")
bill_tree.heading("Product", text="Product")
bill_tree.heading("Quantity", text="Quantity")
bill_tree.heading("Total", text="Total")
bill_tree.pack(pady=10)

# Invoice Frame
invoice_frame = tk.Frame(root)
invoice_frame.pack(pady=10)
tk.Label(invoice_frame, text="Total Amount").grid(row=0, column=0)
total_amount_label = tk.Label(invoice_frame, text="$0.00")
total_amount_label.grid(row=0, column=1)
tk.Button(invoice_frame, text="Generate Invoice", command=generate_invoice).grid(row=1, column=1)

root.mainloop()
