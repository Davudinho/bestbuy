
from typing import List
from products import Product


class Store:
    """Represents a store containing products."""

    def __init__(self, products: list):
        if not isinstance(products, list):
            raise TypeError("products must be a list")
        for p in products:
            if not isinstance(p, Product):
                raise TypeError("all items in products must be Product instances")

        self._products = products

    def add_product(self, product):
        """Adds a Product to the store."""
        if not isinstance(product, Product):
            raise TypeError("product must be a Product instance")

        self._products.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        if not isinstance(product, Product):
            raise TypeError("product must be a Product instance")

        try:
            self._products.remove(product)
        except ValueError:
            raise ValueError("product not found in store")

    def get_total_quantity(self) -> int:
        """Returns total quantity of all products in the store."""
        return sum(p.get_quantity() for p in self._products)

    def get_all_products(self) -> list:
        """Returns a list of active products only."""
        return [p for p in self._products if p.is_active()]

    def order(self, shopping_list: list) -> float:
        """
        Receives a list of (Product, quantity) tuples.
        Buys them and returns total cost.
        """
        if not isinstance(shopping_list, list):
            raise TypeError("shopping_list must be a list")

        total = 0

        for item in shopping_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError("each shopping item must be a tuple (Product, quantity)")

            product, quantity = item

            if not isinstance(product, Product):
                raise TypeError("first element of tuple must be Product")

            total += product.buy(quantity)

        return total
