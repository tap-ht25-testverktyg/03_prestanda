from src.algorithms.search import find_in_list, find_in_list_binary
import pytest

@pytest.fixture(scope="session")
def sorted_list():
    return list(range(10, 100000000, 3))


@pytest.mark.performance
def test_find_in_list__found__benchmark(sorted_list, benchmark):
    actual = benchmark(find_in_list, 19, sorted_list)
    assert actual == True

@pytest.mark.performance
def test_find_in_list__not_found__benchmark(sorted_list, benchmark):
    actual = benchmark(find_in_list, 11, sorted_list)
    assert actual == False


@pytest.mark.performance
def test_find_in_list_binary__found__benchmark(sorted_list, benchmark):
    actual = benchmark(find_in_list_binary, 19, sorted_list)
    assert actual == True

@pytest.mark.performance
def test_find_in_list_binary__not_found__benchmark(sorted_list, benchmark):
    actual = benchmark(find_in_list_binary, 11, sorted_list)
    assert actual == False
