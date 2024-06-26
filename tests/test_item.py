"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item, InstantiateCSVError
import os
import pytest


def test_calculate_total_price():
    item = Item("Shirt", 20.0, 5)
    assert item.calculate_total_price() == 100.0


def test_apply_discount():
    item = Item("Shirt", 20.0, 5)
    Item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 18.0

def test_instantiate_from_csv():
    FILE = "..\\src\\items.csv"
    file_path = os.path.join(os.path.dirname(__file__), FILE)
    items = Item.instantiate_from_csv(file_path)
    assert len(items) == 5
    assert items[0].name == 'Смартфон'
    assert items[0].price == 100
    assert items[1].name == 'Ноутбук'
    assert items[1].price == 1000
    assert items[2].name == 'Кабель'
    assert items[2].price == 10
    assert items[3].name == 'Мышка'
    assert items[3].price == 50
    assert items[4].name == 'Клавиатура'
    assert items[4].price == 75


def test_string_to_number():
    item2 = Item('Телефон', 10000, 5)
    item3 = Item('Apple', 100000, 10)
    assert item2.string_to_number('5') == 5
    assert item2.string_to_number('5.0') == 5
    assert item2.string_to_number('5.5') == 5
    assert item2.string_to_number('10') == 10
    assert item2.string_to_number('10.0') == 10
    assert item2.string_to_number('10.2') == 10
    with pytest.raises(ValueError):
        assert item2.string_to_number("abc") == 10

def test__repr__():
    item2 = Item('Телефон', 10000, 5)
    assert item2.__repr__() == "Item('Телефон', 10000, 5)"
    with pytest.raises(AssertionError):
        assert item2.__repr__() == "Item('Телефон', 20000, 5)"


def test__str__():
    item2 = Item('Телефон', 10000, 5)
    assert item2.__str__() == 'Телефон'
    assert item2.__str__() == str(item2.name)
