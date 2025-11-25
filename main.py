from products import Product
from store import Store


def start(store):
    """Starts the main store menu interface."""

    def list_products():
        for p in store.get_all_products():
            p.show()

    def show_total():
        print("Total quantity:", store.get_total_quantity())

    def make_order():
        products = store.get_all_products()
        shopping_list = []
        print("Enter product numbers to order. 0 to finish.")
        for i, p in enumerate(products, start=1):
            print(i, "-", p._name)

        while True:
            choice = int(input("Product number: "))
            if choice == 0:
                break
            quantity = int(input("Quantity: "))
            shopping_list.append((products[choice - 1], quantity))

        total = store.order(shopping_list)
        print("Order total:", total)

    # Function mapping
    options = {
        "1": list_products,
        "2": show_total,
        "3": make_order,
        "4": exit
    }

    while True:
        print("\n1. List all products")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter choice: ")

        # call function by dictionary
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")

            print("Invalid choice! Please enter a number between 1-4.")


# --- Setup initial stock ---
if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = Store(product_list)

    start(best_buy)
