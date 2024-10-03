import pytest
from task import task_1, task_2, task_3
from unittest.mock import patch

def test_task_1_length():
    result = task_1()
    assert len(result) == 6

def test_task_1_values():
    for test in range(5):
        result = task_1()
        for i in result:
            assert 1 <= i <= 49

def test_task_2_case_90():
    with patch("builtins.input", return_value="90"):
        result = task_2()
        check_list = [i for i in range(100, 89, -1)]
        assert result == check_list

def test_task_2_case_80():
    with patch("builtins.input", return_value="80"):
        result = task_2()
        check_list = [i for i in range(100, 79, -1)]
        assert result == check_list

def test_task_2_case_70():
    with patch("builtins.input", return_value="70"):
        result = task_2()
        check_list = [i for i in range(100, 69, -1)]
        assert result == check_list

def test_task_2_case_60():
    with patch("builtins.input", return_value="60"):
        result = task_2()
        check_list = [i for i in range(100, 59, -1)]
        assert result == check_list

def test_task_3():
    result = task_3
    assert len(result) == 3