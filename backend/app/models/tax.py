from decimal import Decimal

TAXES = [
    ("AL", Decimal("0.04")),
    ("TX", Decimal("0.0625")),
    ("UT", Decimal("0.0685")),
    ("NV", Decimal("0.08")),
    ("CA", Decimal("0.0825")),
]

STATES = [
    "AL",
    "TX",
    "UT",
    "NV",
    "CA",
]


class Tax:
    _state_taxes = dict(TAXES)

    def __init__(self, state: str):
        self.state = state

    def _get_tax_for_state(self) -> Decimal:
        return self._state_taxes.get(self.state, 0)

    def apply(self, price: Decimal) -> Decimal:
        return price + price * self._get_tax_for_state()
