# Define menu items with their prices
menu = {
    'burger': 100,
    'pizza': 150,
    'sandwich': 180,  
    'coffee': 60,
    'fries': 50,
    'veg biryani': 200,  
    'paneer butter masala': 220,  
    'garlic naan': 50,  
    'chapati roti': 30,  
    'steamed rice': 40,  
    'coke': 30,
    'fresh lime soda': 40,  
    'mango lassi': 60,  
    'gulab jamun': 80,  
    'chocolate cake': 120  
}

# function to display the menu
def display_menu():
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item.capitalize()}: ₹{price}")  # Capitalize the first letter of 

# class for managing the cart
class Cart:
    def __init__(self):
        self.items = {}

# function to Add the item to the cart
    def add_item(self, item, quantity=1):
        if item in menu:
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity
        else:
            raise ValueError("Invalid item")
        
# function to remove the item to the cart
    def remove_item(self, item, quantity=1):
        if item in self.items:
            if quantity < 1:
                raise ValueError("Invalid quantity")
            self.items[item] -= quantity
        else:
            raise ValueError("Item not in the cart")
        
# function to display the item in the cart
    def view_cart(self):
        print("\nCart:")
        for item, quantity in self.items.items():
            print(f"{item.capitalize()}: {quantity}")

# function for placing an order and saving it to a file
def place_order(cart):
    cart.view_cart()
    total_amount = 0
    order_details = []

    # Collecting order details
    for item, quantity in cart.items.items():
        price = menu.get(item, 0) * quantity
        total_amount += price
        order_details.append(f"{item.capitalize()}: {quantity} x ₹{menu.get(item)} = ₹{price}")

    order_details.append(f"Total Amount: ₹{total_amount}")

    # Writing order details to a file
    with open("order_details.txt", "w", encoding="utf-8") as file:
        file.write("Order Details:\n")
        file.write("\n".join(order_details))

    print("\nOrder details saved to 'order_details.txt'.")
    print("\nPlease proceed to payment.\nThank you..")


# Main function to run the program
def main():
    cart = Cart()

    while True:
        try:
            action = input("\n1. Add item to cart \n2. Remove item from cart \n3. View cart \n4. Place order \n5. Exit \n")

            if action == '1':
                try:
                    display_menu()  # Display the menu only when adding an item to the cart
                    item = input("\nEnter item to add to cart: ").lower()
                    if item not in menu:
                        raise ValueError("Invalid item")
                    quantity = int(input("Enter quantity: "))
                    if quantity < 1:
                        raise ValueError("Invalid quantity")
                    cart.add_item(item, quantity)
                    print("Item Added Successfully!")
                except ValueError as e:
                    print("Error occurred:", e)
            elif action == '2':
                try:
                    item = input("Enter item to remove from cart: ").lower()
                    if item not in menu:
                        raise ValueError("Invalid item")
                    quantity = int(input("Enter quantity: "))
                    if quantity < 1:
                        raise ValueError("Invalid quantity")
                    cart.remove_item(item, quantity)
                    print("Item Removed Successfully!")
                except ValueError as e:
                    print("Error occurred:", e)
            elif action == '3':
                cart.view_cart() 
            elif action == '4':
                place_order(cart)
                break
            elif action == '5':
                print("\nThank you for using our service!")
                break
            else:
                print("Invalid Action")
        except Exception as e:
            print("Error occurred:", e)

main()
