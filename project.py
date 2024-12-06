import os

# File for storing data
database_file = "database_proj"

# Ensure the file exists
if not os.path.exists(database_file):
    open(database_file, 'w').close()

def display_menu():
    """Display the menu options."""
    print("\n=== Pharmacy Management System ===")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. Search Item")
    print("4. Update Item")
    print("5. View All Items")
    print("6. Exit")

def add_item():
    """Add a new item to the database."""
    item_name = input("Enter item name: ").strip()
    item_price = input("Enter item price: ").strip()
    item_quantity = input("Enter item quantity: ").strip()
    item_category = input("Enter item category: ").strip()
    item_discount = input("Enter item discount: ").strip()

    if not (item_name and item_price and item_quantity and item_category and item_discount):
        print("Error: All fields must be filled!")
        return

    with open(database_file, 'a') as f:
        f.write(f"{item_name},{item_price},{item_quantity},{item_category},{item_discount}\n")
    print("Item added successfully!")

def delete_item():
    """Delete an item by name."""
    item_name = input("Enter the name of the item to delete: ").strip()
    found = False

    with open(database_file, 'r') as f, open("temp_database_proj", 'w') as temp:
        for line in f:
            if line.startswith(item_name + ","):
                found = True
            else:
                temp.write(line)

    os.replace("temp_database_proj", database_file)

    if found:
        print("Item deleted successfully!")
    else:
        print("Error: Item not found!")

def search_item():
    """Search for an item by name."""
    item_name = input("Enter the name of the item to search: ").strip()
    found = False

    with open(database_file, 'r') as f:
        for line in f:
            if line.startswith(item_name + ","):
                data = line.strip().split(",")
                print("\nItem Details:")
                print(f"Name: {data[0]}")
                print(f"Price: {data[1]}")
                print(f"Quantity: {data[2]}")
                print(f"Category: {data[3]}")
                print(f"Discount: {data[4]}")
                found = True
                break

    if not found:
        print("Error: Item not found!")

def update_item():
    """Update an existing item's details."""
    item_name = input("Enter the name of the item to update: ").strip()
    found = False

    with open(database_file, 'r') as f, open("temp_database_proj", 'w') as temp:
        for line in f:
            if line.startswith(item_name + ","):
                found = True
                print("Enter new details (leave blank to keep current value):")
                current_data = line.strip().split(",")
                new_price = input(f"Enter new price (current: {current_data[1]}): ").strip() or current_data[1]
                new_quantity = input(f"Enter new quantity (current: {current_data[2]}): ").strip() or current_data[2]
                new_category = input(f"Enter new category (current: {current_data[3]}): ").strip() or current_data[3]
                new_discount = input(f"Enter new discount (current: {current_data[4]}): ").strip() or current_data[4]
                temp.write(f"{item_name},{new_price},{new_quantity},{new_category},{new_discount}\n")
            else:
                temp.write(line)

    os.replace("temp_database_proj", database_file)

    if found:
        print("Item updated successfully!")
    else:
        print("Error: Item not found!")

def view_all_items():
    """Display all items in the database."""
    print("\n=== All Items ===")
    with open(database_file, 'r') as f:
        lines = f.readlines()
        if not lines:
            print("No items found!")
        else:
            for i, line in enumerate(lines, 1):
                data = line.strip().split(",")
                print(f"{i}. Name: {data[0]}, Price: {data[1]}, Quantity: {data[2]}, Category: {data[3]}, Discount: {data[4]}")

# Main Program
while True:
    display_menu()
    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        add_item()
    elif choice == "2":
        delete_item()
    elif choice == "3":
        search_item()
    elif choice == "4":
        update_item()
    elif choice == "5":
        view_all_items()
    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
