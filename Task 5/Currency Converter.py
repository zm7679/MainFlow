import tkinter as tk
import requests

# Function to fetch exchange rate
def get_exchange_rate(api_url, currency):
    response = requests.get(api_url)
    data = response.json()
    if 'rates' in data and currency in data['rates']:
        return data['rates'][currency]
    else:
        raise Exception("Error fetching exchange rate")

# Function to convert USD to the selected currency
def convert_usd_to_currency(amount, rate):
    return amount * rate

# Function to handle conversion button click
def convert_currency():
    try:
        amount = float(usd_entry.get())
        selected_currency = currency_var.get()
        rate = get_exchange_rate(api_url, selected_currency)
        result = convert_usd_to_currency(amount, rate)
        result_label.config(text=f'{amount} USD = {result:.2f} {selected_currency}')
    except ValueError:
        result_label.config(text="Please enter a valid amount.")
    except Exception as e:
        result_label.config(text=str(e))

# Use a free exchange rate API for testing
api_url = "https://api.exchangerate-api.com/v4/latest/USD"

# Setup the main Tkinter window
window = tk.Tk()
window.title("USD Currency Converter")
window.geometry("300x200")

# USD input field
usd_entry = tk.Entry(window, width=10)
usd_entry.pack(pady=10)

# Dropdown menu for selecting currency
currencies = ["EUR", "INR", "JPY", "GBP"]  # Add more currencies as needed
currency_var = tk.StringVar(window)
currency_var.set(currencies[0])  # Default value
currency_dropdown = tk.OptionMenu(window, currency_var, *currencies)
currency_dropdown.pack(pady=10)

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

# Label to display conversion result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
