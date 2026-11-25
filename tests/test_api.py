"""Тесты для AeroplanesAPI."""

from unittest.mock import Mock, patch

import requests

from src.api import AeroplanesAPI


@patch("src.api.requests.get")
def test_get_country_coordinates(mock_get):
    """Тест получения координат."""
    mock_response = Mock()
    mock_response.json.return_value = [{"boundingbox": ["1", "2", "3", "4"]}]
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    api = AeroplanesAPI()
    result = api.get_country_coordinates("Spain")
    assert result == [1.0, 2.0, 3.0, 4.0]


@patch("src.api.requests.get")
def test_get_country_coordinates_error(mock_get):
    """Тест ошибки при получении координат."""
    mock_get.side_effect = requests.RequestException("Error")
    api = AeroplanesAPI()
    result = api.get_country_coordinates("Spain")
    assert result == []


@patch("src.api.requests.get")
def test_get_country_coordinates_empty(mock_get):
    """Тест: пустой ответ от nominatim."""
    mock_response = Mock()
    mock_response.json.return_value = []
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    api = AeroplanesAPI()
    result = api.get_country_coordinates("Spain")
    assert result == []


@patch("src.api.AeroplanesAPI.get_country_coordinates")
@patch("src.api.requests.get")
def test_get_aeroplanes(mock_get, mock_bbox):
    """Тест получения самолётов."""
    mock_bbox.return_value = [1.0, 2.0, 3.0, 4.0]
    mock_response = Mock()
    mock_response.json.return_value = {"states": [["abc", "UAL1621"]]}
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    api = AeroplanesAPI()
    result = api.get_aeroplanes("Spain")
    assert len(result) == 1


@patch("src.api.AeroplanesAPI.get_country_coordinates")
@patch("src.api.requests.get")
def test_get_aeroplanes_no_bbox(mock_get, mock_bbox):
    """Тест: нет координат — пустой список."""
    mock_bbox.return_value = []
    api = AeroplanesAPI()
    result = api.get_aeroplanes("Spain")
    assert result == []


@patch("src.api.AeroplanesAPI.get_country_coordinates")
@patch("src.api.requests.get")
def test_get_aeroplanes_error(mock_get, mock_bbox):
    """Тест: ошибка при запросе самолётов."""
    mock_bbox.return_value = [1.0, 2.0, 3.0, 4.0]
    mock_get.side_effect = requests.RequestException("Error")
    api = AeroplanesAPI()
    result = api.get_aeroplanes("Spain")
    assert result == []
