import pytest
from src.algorithms.prime import get_primes
from src.algorithms.prime_2 import get_primes_2
from src.algorithms.prime_3 import get_primes_3

@pytest.mark.performance
def test__get_primes__benchmark(benchmark):
    benchmark( get_primes, 3000 )


@pytest.mark.performance
def test__get_primes_2__benchmark(benchmark):
    benchmark( get_primes_2, 3000 )


@pytest.mark.performance
def test__get_primes_3__benchmark(benchmark):
    benchmark( get_primes_3, 3000 )

