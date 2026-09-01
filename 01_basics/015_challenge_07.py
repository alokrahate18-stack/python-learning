laptop_qty = int(input("The total quantity of Laptop purchased: "))
laptop_price = int(input("The price of Laptop purchased: "))
keyboard_qty = int(input("The total quantity of Keyboard purchased: "))
keyboard_price = int(input("The price of Keyboard purchased: "))
mouse_qty = int(input("The total quantity of Mouse purchased: "))
mouse_price = int(input("The price of Mouse purchased: "))

discount = int(input("Discount: "))
delivery = int(input("Delivery charges: "))

laptop_total = laptop_qty * laptop_price
keyboard_total = keyboard_qty * keyboard_price
mouse_total = mouse_qty * mouse_price

sub_total = laptop_total + mouse_total + keyboard_total

taxable = sub_total - discount
gst = taxable + (0.18 * taxable)
gross_total = gst + delivery

print("---------- INVOICE ----------")
print("Laptop       × "+laptop_qty+" : ₹ ", laptop_total)
print("Keyboard     × " +keyboard_qty+ " : ₹ ", keyboard_total)
print("Mouse        × " +mouse_qty+ " : ₹ ", mouse_total)
print("\nSubtotal          : ₹ ", sub_total)
print("Discount          : ₹ ", discount)
print("Taxable           : ₹ ", taxable)
print("GST (18%)         : ₹ ", gst)
print("Delivery          : ₹ ", delivery)
print("\nFinal Amount      : ₹ ", gross_total)
print("-----------------------------")
