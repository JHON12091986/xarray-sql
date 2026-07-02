import pytest
from src.subscript import SubscriptAccess

def test_subscript_column():
    access = SubscriptAccess("table", "column")
    assert access.get_column() == "table.column"

def test_subscript_row():
    access = SubscriptAccess("table", 0)
    assert access.get_row(0) == "table[0]"