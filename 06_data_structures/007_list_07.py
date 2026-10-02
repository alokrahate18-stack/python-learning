"""Advanced: Safe merge and dedupe (lists + references/copying + type conversion + functions)
python
cart_a = ["Pen", "3", "Notebook", "5", "Eraser", "2"]
cart_b = ["notebook", "2", "Pencil", "4", "pen", "1"]

Each list alternates name, quantity as strings. Write merge_carts(cart_a, cart_b) that:

Returns a new flat list in the same [name, qty, name, qty, ...] shape, combining both carts.
Treats names as the same item if they match case-insensitively ("Pen" and "pen" are one item), but keeps the capitalization from whichever cart it saw first.
Adds quantities together as integers, not strings ("3" + "1" must become 4, not "31").
Must not modify cart_a or cart_b at all — prove this to yourself by printing them after calling the function.
Preserves the order items first appeared across both carts combined.
- By Claude"""

def merge_carts(cart_a, cart_b):
    merged_names = []
    merged_qty = []

    for cart in (cart_a, cart_b):
        for i in range(0, len(cart), 2):
            name = cart[i]
            qty = int(cart[i + 1])
            lower_name = name.lower()

            found = False

            for j in range(len(merged_names)):
                if merged_names[j].lower() == lower_name:
                    merged_qty[j] += qty
                    found = True
                    break

            if not found:
                merged_names.append(name)
                merged_qty.append(qty)

    result = []

    for i in range(len(merged_names)):
        result.append(merged_names[i])
        result.append(str(merged_qty[i]))

    return result


cart_a = ["Pen", "3", "Notebook", "5", "Eraser", "2"]
cart_b = ["notebook", "2", "Pencil", "4", "pen", "1"]

merged = merge_carts(cart_a, cart_b)

print("Merged:", merged)
print("cart_a:", cart_a)
print("cart_b:", cart_b)

