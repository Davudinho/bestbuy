class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Name darf nicht leer sein")
        if price < 0:
            raise ValueError("Preis darf nicht negativ sein")
        if quantity < 0:
            raise ValueError("Menge darf nicht negativ sein")

        self.name = name
        self.price = price
        self._quantity = quantity
        self._active = True if quantity > 0 else False

    # Getter für Menge
    def get_quantity(self) -> int:
        return self._quantity

    # Setter für Menge
    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()
        else:
            self.activate()

    # Getter für Aktiv-Status
    def is_active(self) -> bool:
        return self._active

    # Aktivieren
    def activate(self):
        self._active = True

    # Deaktivieren
    def deactivate(self):
        self._active = False

    # Produktinfo ausgeben
    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self._quantity}")

    # Kaufen
    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Die Kaufmenge muss größer als 0 sein")
        if quantity > self._quantity:
            raise ValueError(f"Nicht genug {self.name} auf Lager")

        total_price = self.price * quantity
        self._quantity -= quantity
        if self._quantity == 0:
            self.deactivate()
        return total_price
