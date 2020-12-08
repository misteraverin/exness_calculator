from decimal import Decimal
from app.models.tax import Tax
from app.models.discount import Discount


class Calculator:
    def __init__(self, state: str, product_quantity: int, price: Decimal):
        self.state = state
        self.product_quantity = product_quantity
        self.price = price

    def calculate_total_order_price(self) -> Decimal:
        total_order_price = self.price * self.product_quantity
        discounted_price = Discount.apply(total_order_price)
        total_price_with_tax = Tax(self.state).apply(discounted_price)
        return total_price_with_tax
