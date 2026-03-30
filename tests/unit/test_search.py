from src.algorithms.search import find_in_list
import pytest

@pytest.fixture(scope="session")
def sorted_list():
    return list(range(10, 100, 3))


@pytest.mark.unit
def test_find_in_list__found(sorted_list):
    # print(sorted_list)
    assert find_in_list(19, sorted_list) == True


@pytest.mark.unit
def test_find_in_list__not_found(sorted_list):
    assert find_in_list(11, sorted_list) == False



@pytest.mark.unit
def test_find_in_list_binary__found(sorted_list):
    # print(sorted_list)
    assert find_in_list(19, sorted_list) == True


@pytest.mark.unit
def test_find_in_list_binary__not_found(sorted_list):
    assert find_in_list(11, sorted_list) == False

