"""Тесты для класса Aeroplane."""

import pytest

from src.aeroplane import Aeroplane


def test_aeroplane_init():
    """Тест инициализации."""
    plane = Aeroplane("UAL1621", "United States", 268.79, 10203.18)
    assert plane.callsign == "UAL1621"
    assert plane.country == "United States"
    assert plane.speed == 268.79
    assert plane.altitude == 10203.18


def test_aeroplane_invalid_callsign():
    """Тест: пустой позывной — ValueError."""
    with pytest.raises(ValueError):
        Aeroplane("", "United States", 100.0, 1000.0)


def test_aeroplane_invalid_country():
    """Тест: пустая страна — ValueError."""
    with pytest.raises(ValueError):
        Aeroplane("UAL1621", "", 100.0, 1000.0)


def test_aeroplane_invalid_speed():
    """Тест: отрицательная скорость — ValueError."""
    with pytest.raises(ValueError):
        Aeroplane("UAL1621", "United States", -100.0, 1000.0)


def test_aeroplane_invalid_altitude():
    """Тест: отрицательная высота — ValueError."""
    with pytest.raises(ValueError):
        Aeroplane("UAL1621", "United States", 100.0, -1000.0)


def test_aeroplane_str():
    """Тест строкового отображения."""
    plane = Aeroplane("UAL1621", "US", 100.0, 1000.0)
    assert "UAL1621" in str(plane)
    assert "US" in str(plane)


def test_aeroplane_comparison_speed():
    """Тест сравнения по скорости."""
    a = Aeroplane("A", "US", 100.0, 1000.0)
    b = Aeroplane("B", "US", 200.0, 1000.0)
    assert a < b


def test_aeroplane_comparison_altitude():
    """Тест сравнения по высоте."""
    a = Aeroplane("A", "US", 100.0, 2000.0)
    b = Aeroplane("B", "US", 100.0, 1000.0)
    assert a > b


def test_aeroplane_equality():
    """Тест равенства."""
    a = Aeroplane("A", "US", 100.0, 1000.0)
    b = Aeroplane("B", "US", 100.0, 1000.0)
    assert a == b


def test_cast_to_object_list():
    """Тест преобразования списка из API."""
    raw = [
        [
            "abc",
            "UAL1621",
            "United States",
            None,
            None,
            None,
            None,
            None,
            None,
            268.79,
            None,
            None,
            None,
            10203.18,
        ],
        [
            "def",
            "QQE933",
            "Qatar",
            None,
            None,
            None,
            None,
            None,
            None,
            268.24,
            None,
            None,
            None,
            13746.48,
        ],
    ]
    result = Aeroplane.cast_to_object_list(raw)
    assert len(result) == 2
    assert result[0].callsign == "UAL1621"
    assert result[1].country == "Qatar"


def test_cast_to_object_list_invalid():
    """Тест: некорректные данные в cast_to_object_list."""
    raw = [
        ["abc"],
        [
            "def",
            "",
            "US",
            None,
            None,
            None,
            None,
            None,
            None,
            100.0,
            None,
            None,
            None,
            1000.0,
        ],
    ]
    result = Aeroplane.cast_to_object_list(raw)
    assert len(result) == 0
