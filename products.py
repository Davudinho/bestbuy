class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name darf nicht leer sein")
        if price < 0 or quantity < 0:
            raise ValueError("Preis und Menge dürfen nicht negativ sein")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    # Methode, um Produkte zu kaufen
    def buy(self, amount):
        if amount > self.quantity:
            return f"Not enough {self.name} in stock!"
        self.quantity -= amount
        return f"{amount} units of {self.name} bought. Remaining: {self.quantity}"

    # Prüfen, ob das Produkt aktiv ist
    def is_active(self):
        return self.active

    # Zeige Produktinformationen
    def show(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Active: {self.active}")

    # Menge ändern
    def set_quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = new_quantity
