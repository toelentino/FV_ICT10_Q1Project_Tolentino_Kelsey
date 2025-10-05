from pyscript import display 

# for this part, i just declared the variables since the computation will be in the other python file. :)

store_name = "The Pining Shelf"        # STRING: name of the store
branch_location = "Manila, Philippines" # STRING: branch location
manager_name = "Kelsey Sasha G. Tolentino"  # STRING: manager/owner
year_opened = 2025                     # INTEGER: year opened
has_online_orders = True               # BOOLEAN: online ordering available
delivery_fee = 50.00                   # FLOAT: delivery fee in pesos
business_hours = "10 AM - 11 PM"       # STRING: operating hours

# Inventory / Products 

book_titles = ["One Piece", "Fruits Basket", "Bleach", "Horimiya", "Kimi ni Todoke"]  # LIST: product names
book_prices = [599.00, 500.00, 599.00, 550.00, 500.00]                                # LIST: product prices
stock_count = 100                     # INTEGER: total stock available
tax_rate = 0.07                       # FLOAT: 7% tax rate

# I wanted to display my information so that people can see, so I used the display code

display(f"🐱 Welcome to {store_name} - {branch_location}", target="output")
display(f"Manager: {manager_name}", target="output")
display(f"Opened in: {year_opened}", target="output")
display(f"Business Hours: {business_hours}", target="output")