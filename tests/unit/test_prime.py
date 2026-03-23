import pytest
from src.algorithms.prime import is_prime

pytestmark = pytest.mark.unit


def test__is_prime__returns_true():
    # Act
    result = is_prime(5)

    # Assert
    assert result == True


def test__is_prime__returns_false():
    result = is_prime(10)
    assert result == False
