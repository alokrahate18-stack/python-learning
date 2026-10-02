"""Q1: Inventory shell with undo (lists + match-case + functions + strings + loops)

Build a command shell that loops until the user types quit. Use only lists (no dicts): one list for item names and a parallel list for quantities. Read each line with input(), .split() it, and dispatch with match/case using *rest patterns and if guards. Every command must live in its own function.

add <qty> <name...>: the name may have several words (add 5 green apples). qty must be a positive whole number. If the item already exists (case-insensitive), increase it.
take <qty> <name...>: reduce the quantity. If the request is more than available, reject it and print exactly how many are available. If it reaches 0, remove the item.
remove <name...>: delete the item entirely.
undo: reverse the last successful change, repeatedly, back to the start. Removed items must come back at their original position.
show: print items sorted by quantity descending, then name ascending, without changing the stored order (or undo will break).
Unknown commands and malformed input must print a helpful message, never crash. It must survive add ² apples and add 3 and an empty line.
- By Claude"""

def find_item_index(names, item_name):
    """Return the index of item_name, ignoring case; otherwise return -1."""
    target = item_name.lower()

    for i in range(len(names)):
        if names[i].lower() == target:
            return i

    return -1


def is_positive_whole_number(text):
    """Accept only ordinary ASCII digits representing an integer greater than 0."""
    return text.isascii() and text.isdigit() and int(text) > 0


def make_name(name_parts):
    """Turn ['green', 'apples'] into 'green apples'."""
    return " ".join(name_parts)


def add_item(names, quantities, history, qty_text, name_parts):
    quantity = int(qty_text)
    item_name = make_name(name_parts)
    index = find_item_index(names, item_name)

    if index == -1:
        names.append(item_name)
        quantities.append(quantity)

        # Undo action: delete the new item from its stored position.
        history.append(["add_new", len(names) - 1])

        print(f"Added {quantity} {item_name}.")
    else:
        quantities[index] += quantity

        # Undo action: subtract exactly what this command added.
        history.append(["add_existing", index, quantity])

        print(f"Added {quantity} to {names[index]}. Total: {quantities[index]}.")


def take_item(names, quantities, history, qty_text, name_parts):
    quantity = int(qty_text)
    item_name = make_name(name_parts)
    index = find_item_index(names, item_name)

    if index == -1:
        print(f"Item not found: {item_name}.")
        return

    available = quantities[index]

    if quantity > available:
        print(f"Cannot take {quantity} {names[index]}; only {available} available.")
        return

    if quantity < available:
        quantities[index] -= quantity

        # Undo action: add back the quantity taken.
        history.append(["take_partial", index, quantity])

        print(f"Took {quantity} from {names[index]}. Remaining: {quantities[index]}.")
    else:
        removed_name = names.pop(index)
        removed_quantity = quantities.pop(index)

        # Undo needs the full item and its original position.
        history.append(["take_all", index, removed_name, removed_quantity])

        print(f"Took {quantity} {removed_name}. Item removed.")


def remove_item(names, quantities, history, name_parts):
    item_name = make_name(name_parts)
    index = find_item_index(names, item_name)

    if index == -1:
        print(f"Item not found: {item_name}.")
        return

    removed_name = names.pop(index)
    removed_quantity = quantities.pop(index)

    # Store index so undo restores the original stored order.
    history.append(["remove", index, removed_name, removed_quantity])

    print(f"Removed {removed_name} ({removed_quantity}).")


def undo_last_change(names, quantities, history):
    if not history:
        print("Nothing to undo.")
        return

    action = history.pop()
    kind = action[0]

    match kind:
        case "add_new":
            index = action[1]
            removed_name = names.pop(index)
            quantities.pop(index)
            print(f"Undid add: removed {removed_name}.")

        case "add_existing":
            index = action[1]
            quantity = action[2]
            quantities[index] -= quantity
            print(f"Undid add: removed {quantity} from {names[index]}.")

        case "take_partial":
            index = action[1]
            quantity = action[2]
            quantities[index] += quantity
            print(f"Undid take: restored {quantity} to {names[index]}.")

        case "take_all":
            index = action[1]
            item_name = action[2]
            quantity = action[3]
            names.insert(index, item_name)
            quantities.insert(index, quantity)
            print(f"Undid take: restored {item_name} ({quantity}).")

        case "remove":
            index = action[1]
            item_name = action[2]
            quantity = action[3]
            names.insert(index, item_name)
            quantities.insert(index, quantity)
            print(f"Undid remove: restored {item_name} ({quantity}).")


def show_items(names, quantities):
    if not names:
        print("Inventory is empty.")
        return

    # Create a separate sortable list. Do not rearrange names/quantities,
    # because their stored order is required for correct undo behavior.
    display_items = []

    for i in range(len(names)):
        display_items.append([names[i], quantities[i]])

    # Sort only the separate display list:
    # quantity descending; name ascending, case-insensitively.
    display_items.sort(key=lambda item: (-item[1], item[0].lower()))

    for item in display_items:
        print(f"{item[0]}: {item[1]}")


def print_help():
    print("Commands:")
    print("  add <qty> <name...>")
    print("  take <qty> <name...>")
    print("  remove <name...>")
    print("  undo")
    print("  show")
    print("  quit")


def run_inventory_shell():
    names = []
    quantities = []
    history = []

    print("Inventory shell. Type 'help' for commands.")

    while True:
        try:
            parts = input("> ").split()
        except EOFError:
            print("\nGoodbye.")
            break

        match parts:
            case []:
                print("Please enter a command.")

            case ["quit"]:
                print("Goodbye.")
                break

            case ["help"]:
                print_help()

            case ["show"]:
                show_items(names, quantities)

            case ["undo"]:
                undo_last_change(names, quantities, history)

            case ["add", qty_text, *rest] if rest and is_positive_whole_number(qty_text):
                add_item(names, quantities, history, qty_text, rest)

            case ["take", qty_text, *rest] if rest and is_positive_whole_number(qty_text):
                take_item(names, quantities, history, qty_text, rest)

            case ["remove", *rest] if rest:
                remove_item(names, quantities, history, rest)

            case ["add", *_]:
                print("Usage: add <positive whole number> <name...>")

            case ["take", *_]:
                print("Usage: take <positive whole number> <name...>")

            case ["remove", *_]:
                print("Usage: remove <name...>")

            case _:
                print("Unknown command. Type 'help' for valid commands.")


run_inventory_shell()
