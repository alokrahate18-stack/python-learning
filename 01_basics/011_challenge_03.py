print("Product Purchase Calculator")

product_cost = float(input("Enter the cost of the product: "))
product_quantity = int(input("Enter the quantity of the product: "))
total_cost = product_cost * product_quantity
print(f"The total cost of the product is: Rs.{total_cost:.2f}")
discount = float(input("Enter the discount percentage (if any, else enter 0): "))
if discount > 0:
    discount_amount = total_cost * (discount / 100)
    total_cost -= discount_amount
    print(f"Discount applied: Rs.{discount_amount:.2f}")
elif discount < 0:
    print("Invalid discount percentage. Please enter a positive value.")
else:
    print("No discount applied.")

print("18% tax will be added to the total cost.")
tax_amount = total_cost * 0.18
total_cost += tax_amount
print(f"Tax applied: Rs.{tax_amount:.2f}")
print(f"The final cost of the product is: Rs.{total_cost:.2f}")
