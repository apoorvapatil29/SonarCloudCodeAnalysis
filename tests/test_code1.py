# tests/test_your_code.py
from src.codes1 import multiply_numbers

import pytest
from src.codes1 import multiply_numbers

def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-1, 1) == -1
    assert multiply_numbers(0, 5) == 0
