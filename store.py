# store.py
from typing import List
from products import Product  # Stelle sicher, dass die Product-Klasse in products.py definiert ist


class Store:
    def __init__(self, products: List[Product] = None):
        if products is None:
            products = []
        self.products = products  # Liste aller Produkte im Store

    # Produkt hinzufügen
    def add_product(self, product: Product):
        self.products.append(product)

    # Produkt entfernen
    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    # Gesamtmenge aller Produkte im Store (nur aktive)
    def get_total_quantity(self) -> int:
        return sum(p.get_quantity() for p in self.products if p.is_active())

    # Alle aktiven Produkte zurückgeben
    def get_all_products(self) -> List[Product]:
        return [p for p in self.products if p.is_active()]

    # Bestellung ausführen
    # shopping_list: Liste von Tupeln (Produkt, Menge)
    def order(self, shopping_list: List[tuple]) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError(f"Product {product.name} not in store")
            if not product.is_active():
                raise ValueError(f"Product {product.name} is not active")
            total_price += product.buy(quantity)
        return total_price


# --- Testcode ---
if __name__ == "__main__":
    import product as products

    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    products_active = best_buy.get_all_products()
    print("Total quantity in store:", best_buy.get_total_quantity())

    price = best_buy.order([(products_active[0], 1), (products_active[1], 2)])
    print(f"Order cost: {price} dollars.")

    print("Remaining total quantity:", best_buy.get_total_quantity())
