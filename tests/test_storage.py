"""Тесты для JSONSaver."""

import pytest

from src.aeroplane import Aeroplane
from src.storage import JSONSaver


@pytest.fixture
def saver(tmp_path):
    """Фикстура с временным файлом."""
    return JSONSaver(str(tmp_path / "test.json"))


@pytest.fixture
def aeroplane():
    """Фикстура с самолётом."""
    return Aeroplane("UAL1621", "United States", 268.79, 10203.18)


def test_add_aeroplane(saver, aeroplane):
    """Тест добавления."""
    saver.add_aeroplane(aeroplane)
    data = saver._load()
    assert len(data) == 1
    assert data[0]["callsign"] == "UAL1621"


def test_delete_aeroplane(saver, aeroplane):
    """Тест удаления."""
    saver.add_aeroplane(aeroplane)
    saver.delete_aeroplane(aeroplane)
    data = saver._load()
    assert len(data) == 0


def test_get_aeroplanes(saver, aeroplane):
    """Тест получения по критериям."""
    saver.add_aeroplane(aeroplane)
    result = saver.get_aeroplanes({"country": "United States"})
    assert len(result) == 1
