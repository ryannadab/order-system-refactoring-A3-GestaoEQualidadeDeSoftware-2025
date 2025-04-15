# order_system_refactored.py

from abc import ABC, abstractmethod

class Item:
    def _init_(self, name: str, price: float):
        self.name = name
        self.price = price

class Customer:
    def _init_(self, name: str):
        self.name = name

class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, order_total: float) -> float:
        pass

class LocalShipping(ShippingStrategy):
    def calculate(self, order_total: float) -> float:
        return 10.0

class NationalShipping(ShippingStrategy):
    def calculate(self, order_total: float) -> float:
        return 20.0

class InternationalShipping(ShippingStrategy):
    def calculate(self, order_total: float) -> float:
        return 50.0

class Order:
    def _init_(self, customer: Customer, items: list[Item], shipping_strategy: ShippingStrategy):
        self.customer = customer
        self.items = items
        self.shipping_strategy = shipping_strategy

    def total(self) -> float:
        return sum(item.price for item in self.items)

    def shipping_cost(self) -> float:
        return self.shipping_strategy.calculate(self.total())

    def final_total(self) -> float:
        return self.total() + self.shipping_cost()

    def print_invoice(self):
        print(f"Pedido para: {self.customer.name}")
        for item in self.items:
            print(f"{item.name} - R${item.price}")
        print(f"Subtotal: R${self.total()}")
        print(f"Frete: R${self.shipping_cost()}")
        print(f"Total final: R${self.final_total()}")

# Exemplo de uso
if __name__ == "_main_":
    items = [
        Item("Notebook", 3000),
        Item("Mouse", 150),
        Item("Teclado", 200)
    ]

    customer = Customer("Maria")

    # Substitua aqui para testar outros tipos de frete
    shipping = NationalShipping()

    order = Order(customer, items, shipping)
    order.print_invoice()

    #Commit feito