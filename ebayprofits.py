import tkinter as tk

# Dictionary of categories and their corresponding fees
category_fees = {
    'Most categories': [0.1325, 0.0235, 7500],
    'Books & Magazines': [0.1495, 0.0235, 7500],
    'Coins & Paper Money > Bullion': [0.1325, 0.07, 7500],
    'Women\'s Bags & Handbags': [0.15, 0.09, 2000],
    'Jewelry & Watches (except Watches, Parts & Accessories)': [0.15, 0.09, 5000],
    'Watches, Parts & Accessories': [0.15, 0.065, 7500],
    'NFTs': [0.05, 0, 0],
    'Select Business & Industrial categories': [0.03, 0.005, 15000],
    'Musical Instruments & Gear > Guitars & Basses': [0.0635, 0.0235, 7500],
    'Select Clothing, Shoes & Accessories categories': [0.1325, 0, 0]
}

# Define the function to calculate the profit
def calculate_profit():
    try:
        # Get the input values from the user
        selling_price = float(selling_price_entry.get())
        item_cost = float(item_cost_entry.get())
        shipping_cost = float(shipping_cost_entry.get())
        promotional_cost = float(promotional_cost_entry.get())/100

        # Calculate the eBay fee based on the selected category
        category = category_var.get()
        category_fee = category_fees[category]
        if selling_price <= category_fee[2]:
            ebay_fee = selling_price * category_fee[0]
        else:
            ebay_fee = category_fee[2] * category_fee[0] + (selling_price - category_fee[2]) * category_fee[1]

        # Calculate the profit and profit percentage
        profit = selling_price - item_cost - shipping_cost - selling_price * promotional_cost - ebay_fee
        profit_percentage = profit / selling_price * 100

        # Display the profit and profit percentage in the output label
        output_label.config(text=f"Profit: ${profit:.2f}\nProfit Percentage: {profit_percentage:.2f}%")

        # Clear the terminal and display the breakdown of the math
        terminal_text.delete('1.0', tk.END)
        terminal_text.insert(tk.END, f"Selling Price: ${selling_price:.2f}\n")
        terminal_text.insert(tk.END, f"Item Cost: ${item_cost:.2f}\n")
        terminal_text.insert(tk.END, f"Shipping Cost: ${shipping_cost:.2f}\n")
        terminal_text.insert(tk.END, f"Promotional Cost: {promotional_cost * 100:.2f}% (${selling_price * promotional_cost:.2f})\n")
        terminal_text.insert(tk.END, f"eBay Fee: ${ebay_fee:.2f}\n")
        terminal_text.insert(tk.END, f"Subtractions: ${selling_price:.2f} - ${item_cost:.2f} - ${shipping_cost:.2f} - ${selling_price * promotional_cost:.2f} - ${ebay_fee:.2f} = ${profit:.2f}\n")
    except ValueError:
        # Display an error message if the input values are invalid
        output_label.config(text="Please enter valid numbers for all fields")

# Create a GUI with a dropdown list of categories and input fields for the selling price, item cost, shipping cost, and promotional cost
root = tk.Tk()
root.title("eBay Profit Calculator")

# Create the category dropdown list
category_var = tk.StringVar(value=list(category_fees.keys())[0])
category_label = tk.Label(root, text="Category (FVFs as of February 17th, 2023):")
category_label.pack()
category_menu = tk.OptionMenu(root, category_var, *category_fees.keys())
category_menu.pack()

# Create the input fields
selling_price_label = tk.Label(root, text="Selling Price:")
selling_price_label.pack()
selling_price_entry = tk.Entry(root)
selling_price_entry.pack()

item_cost_label = tk.Label(root, text="Item Cost:")
item_cost_label.pack()
item_cost_entry = tk.Entry(root)
item_cost_entry.pack()

shipping_cost_label = tk.Label(root, text="Shipping/Packaging/Handling Costs:")
shipping_cost_label.pack()
shipping_cost_entry = tk.Entry(root)
shipping_cost_entry.pack()

promotional_cost_label = tk.Label(root, text="Promotional Cost (% of Selling Price):")
promotional_cost_label.pack()
promotional_cost_entry = tk.Entry(root)
promotional_cost_entry.pack()

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_profit)
calculate_button.pack()

# Create the output label
output_label = tk.Label(root, text="")
output_label.pack()

# Create a terminal to display the breakdown of the math
terminal = tk.Frame(root, bd=1, relief="sunken")
terminal.pack(fill="both", expand=True)
terminal_label = tk.Label(terminal, text="Breakdown of Math:")
terminal_label.pack(side="top", fill="both")
terminal_text = tk.Text(terminal, height=5)
terminal_text.pack(side="top", fill="both", expand=True)

# Redirect stdout to the terminal
import sys

class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, str):
        self.text_widget.insert("end", str)
        self.text_widget.see("end")

sys.stdout = StdoutRedirector(terminal_text)

root.mainloop()

