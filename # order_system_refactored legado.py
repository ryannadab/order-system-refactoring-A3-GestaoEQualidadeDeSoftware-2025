import unittest
from abc import ABC, abstractmethod

class Item:
    """Representa um item individual em um pedido."""
    def __init__(self, name: str, price: float):
        """
        Inicializa um novo item.

        Args:
            name (str): O nome do item.
            price (float): O preço do item.
        """
        self.name = name
        self.price = price

class Customer:
    """Representa um cliente que faz um pedido."""
    def __init__(self, name: str):
        """
        Inicializa um novo cliente.

        Args:
            name (str): O nome do cliente.
        """
        self.name = name

class ShippingStrategy(ABC):
    """Interface para definir a estratégia de cálculo do custo de frete."""
    @abstractmethod
    def calculate(self, order_total: float) -> float:
        """
        Calcula o custo de frete para um determinado total do pedido.

        Args:
            order_total (float): O valor total dos itens no pedido.

        Returns:
            float: O custo de frete.
        """
        pass

class LocalShipping(ShippingStrategy):
    """Estratégia de frete para entregas locais."""
    def calculate(self, order_total: float) -> float:
        """Calcula o custo de frete para entregas locais (valor fixo)."""
        return 10.0

class NationalShipping(ShippingStrategy):
    """Estratégia de frete para entregas nacionais."""
    def calculate(self, order_total: float) -> float:
        """Calcula o custo de frete para entregas nacionais (valor fixo)."""
        return 20.0

class InternationalShipping(ShippingStrategy):
    """Estratégia de frete para entregas internacionais."""
    def calculate(self, order_total: float) -> float:
        """Calcula o custo de frete para entregas internacionais (valor fixo)."""
        return 50.0

class Order:
    """Representa um pedido feito por um cliente, contendo itens e uma estratégia de frete."""
    def __init__(self, customer: Customer, items: list[Item], shipping_strategy: ShippingStrategy):
        """
        Inicializa um novo pedido.

        Args:
            customer (Customer): O cliente que fez o pedido.
            items (list[Item]): Uma lista dos itens no pedido.
            shipping_strategy (ShippingStrategy): A estratégia de frete a ser aplicada.
        """
        self.customer = customer
        self.items = items
        self.shipping_strategy = shipping_strategy

    def calculate_total(self) -> float:
        """Calcula o valor total dos itens no pedido."""
        return sum(item.price for item in self.items)

    def calculate_shipping_cost(self) -> float:
        """Calcula o custo de frete para o pedido usando a estratégia definida."""
        return self.shipping_strategy.calculate(self.calculate_total())

    def calculate_final_total(self) -> float:
        """Calcula o valor total final do pedido, incluindo o frete."""
        return self.calculate_total() + self.calculate_shipping_cost()

    def print_invoice(self):
        """Imprime a fatura do pedido com detalhes do cliente, itens, subtotal, frete e total final."""
        print(f"Pedido para: {self.customer.name}")
        for item in self.items:
            print(f"{item.name} - R${item.price:.2f}")
        print(f"Subtotal: R${self.calculate_total():.2f}")
        print(f"Frete: R${self.calculate_shipping_cost():.2f}")
        print(f"Total final: R${self.calculate_final_total():.2f}")

# Exemplo de uso
if __name__ == "__main__":
    items = [
        Item("Notebook", 3000.00),
        Item("Mouse", 150.50),
        Item("Teclado", 200.00)
    ]

    customer = Customer("Maria")

    # Substitua aqui para testar outros tipos de frete
    shipping = NationalShipping()

    order = Order(customer, items, shipping)
    order.print_invoice()