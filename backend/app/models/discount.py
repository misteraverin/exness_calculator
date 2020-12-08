from decimal import Decimal

DISCOUNTS = [
    (0, Decimal("0")),
    (1000, Decimal("0.03")),
    (5000, Decimal("0.05")),
    (7000, Decimal("0.07")),
    (10000, Decimal("0.1")),
    (50000, Decimal("0.15")),
]


class Discount:
    _discounts = sorted(DISCOUNTS)

    @classmethod
    def _get_discount(cls, price: Decimal) -> Decimal:
        if price <= 0:
            return Decimal("0")

        last_percentage = 0
        for bound_price, discount in cls._discounts:
            if price < bound_price:
                break
            last_percentage = discount

        return last_percentage

    @classmethod
    def apply(cls, price: Decimal) -> Decimal:
        return price - price * cls._get_discount(price)
