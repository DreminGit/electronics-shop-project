"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item, InstantiateCSVError
from src.phone import Phone
from src.hard import Hard
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