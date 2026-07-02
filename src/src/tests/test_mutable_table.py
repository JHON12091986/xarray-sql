import pytest
from src.mutable_table import MutableTable

def test_mutable_table_append():
    table = MutableTable("test", ["id", "value"])
    table.append([1, 10])
    table.append([2, 20])
    assert len(table.get_state()) == 2

def test_mutable_table_clear():
    table = MutableTable("test", ["id", "value"])
    table.append([1, 10])
    table.clear()
    assert len(table.get_state()) == 0