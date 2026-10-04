#week_5_lab.py
#Author: Brenden Canale
#Business Domain: Tech

product_name = 'laptop' # str
status = 'pending' # str
quantity = 3 # int
unit_price = 450.00 # float
is_over_limit = unit_price * quantity > 1000 # boolean

print(type(product_name), type(quantity), type(unit_price), type(is_over_limit))

subtotal = unit_price * quantity #expected 1350.00
tax = subtotal * 0.07 #expected: 94.50
total = subtotal + tax #expected 1444.50
requires_approval = total > 1000 #expected true

print("=== Purchase Request Summary ===")
print(f"Product: {product_name}")
print(f"Qty: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: {total:.2f}")
print(f"Requires approval: {requires_approval}")

#Step 6

user_qty = int(input("Enter in a new quantity: "))
new_total = unit_price * user_qty * 1.07
print(f"New total for {user_qty} units: ${new_total:.2f}")
print(f"Requires approval: {new_total > 1000}")