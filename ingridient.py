class Ingrigient:
    def __init__(self, name, quantity, unit):
        self.name=name
        self.quantity=quantity
        self.unit=unit
    @property
    def quantity(self):
        return self.quantity
    @quantity.setter
    def quantity(self, value):
        if value<=0:
            raise ValueError("Количество должно быть положительным")
        self.quantity=float(value)
    def __str__(self):
        return f"{self.name}:{self.quantity} {self.unit}"
    def __repr__(self):
        return f"Ingrigient('{self.name}', {self.quantity}, {self.unit})"
    def __eq__(self, other):
        if type(other)!=Ingrigient:
            return False
        return self.name==other.name and self.unit==other.unit







