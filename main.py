
from products import Product
from store import Store

def start(store: Store):
    while True:
        print("\n--- Welcome to the Store ---")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nAvailable products:")
            for product in store.get_all_products():
                product.show()

        elif choice == "2":
            total_quantity = store.get_total_quantity()
            print(f"\nTotal quantity of active products in store: {total_quantity}")

        elif choice == "3":
            print("\nEnter your order:")
            shopping_list = []
            while True:
                name = input("Product name (or 'done' to finish): ")
                if name.lower() == "done":
                    break
                quantity_str = input("Quantity: ")
                if not quantity_str.isdigit():
                    print("Invalid quantity, must be a number!")
                    continue
                quantity = int(quantity_str)

                # Finde das Produkt im Store
                product_found = None
                for product in store.get_all_products():
                    if product.name.lower() == name.lower():
                        product_found = product
                        break

                if product_found is None:
                    print(f"Product '{name}' not found or not active!")
                    continue

                shopping_list.append((product_found, quantity))

            # Bestellung ausführen
            if shopping_list:
                try:
                    total_price = store.order(shopping_list)
                    print(f"Order completed! Total cost: ${total_price}")
                except ValueError as e:
                    print(f"Error: {e}")

        elif choice == "4":
            print("Thank you for visiting!")
            break

        else:
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
