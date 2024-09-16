import pytest
from task import task_1, task_2, task_3
from unittest.mock import patch

def test_task_1_length():
    result = task_1()
    assert len(result) == 6

@pytest.mark.parametrize("n", range(10))
def test_task_1_values(n):
    result = task_1()
    for i in result:
        assert 1 <= i <= 49

@pytest.mark.parametrize("endpoint", [90, 80, 70, 60])
def test_task_2(endpoint):
    with patch("builtins.input", return_value=(str(endpoint))):
        result = task_2()
        check_list = [i for i in range(100, endpoint - 1, -1)]
        assert result == check_list

def test_task_3():
    result = task_3
    assert len(result) == 3