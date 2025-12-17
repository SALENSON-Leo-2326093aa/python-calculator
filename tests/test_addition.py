import pytest
from src.calculator import add

def test_add():
    assert add(3, 4) == 7

def test_add_string():
    with pytest.raises(TypeError):
        add("string", 4)
