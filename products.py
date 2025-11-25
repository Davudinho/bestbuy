class Product:
    """Represents a product sold in the store."""

    def __init__(self, name: str, price: float, quantity: int):
        # --- Type Checks ---
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(price, (float, int)):
            raise TypeError("price must be a number")
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")

        # --- Value Checks ---
        if name.strip() == "":
            raise ValueError("name cannot be empty")
        if price < 0:
            raise ValueError("price cannot be negative")
        if quantity < 0:
            raise ValueError("quantity cannot be negative")

        # --- Assign values ---
        self._name = name
        self._price = float(price)
        self._quantity = quantity
        self._active = True

    def get_quantity(self) -> int:
        """Returns the available quantity of the product."""
        return self._quantity

    def set_quantity(self, quantity: int):
        """Sets the product quantity and deactivates it if quantity becomes 0."""
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")
        if quantity < 0:
            raise ValueError("quantity cannot be negative")

        self._quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns True if the product is active."""
        return self._active

    def activate(self):
        """Activates the product."""
        self._active = True

    def deactivate(self):
        """Deactivates the product."""
        self._active = False

    def show(self):
        """Prints a string representation of the product."""
        print(f"{self._name}, Price: {self._price}, Quantity: {self._quantity}")

    def buy(self, quantity: int) -> float:
        """Buys a quantity of the product and returns total price."""
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")
        if quantity <= 0:
            raise ValueError("quantity must be positive")

        if quantity > self._quantity:
            raise ValueError("Not enough products in stock")

        total_price = quantity * self._price
        self._quantity -= quantity

        if self._quantity == 0:
            self.deactivate()

        return total_price
