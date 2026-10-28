
import pytest
from app import calculate_total

def test_calculate_total_with_discount():
    assert calculate_total(50, 2, 10) == 90.0
    assert calculate_total(10.5, 2, 0) == 21.0

def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_total(10, 2, 150)
