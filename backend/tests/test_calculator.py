import pytest

from decimal import Decimal
from app.calculator import Calculator


@pytest.mark.parametrize(
    "test_value,expected_result",
    [
        (("UK", 12, 13), Decimal("156")),
        (("UT", 100, 13), Decimal("1347.3785")),
        (("NV", 6000, 1), Decimal("6156")),
        (("CA", 7456, 1), Decimal("7506.1416")),
        (("AL", 13000, 3), Decimal("36504")),
        (("TX", 50000, 10), Decimal("451562.5")),
    ],
)
def test_calculate_total_order_price(test_value, expected_result):
    calculator = Calculator(*test_value)
    assert expected_result == calculator.calculate_total_order_price()
