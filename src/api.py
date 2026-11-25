"""Модуль для работы с API самолётов."""

from abc import ABC, abstractmethod
from typing import Any

import requests


class BaseAPI(ABC):
    """Абстрактный класс для работы с API."""

    @abstractmethod
    def get_country_coordinates(self, country: str) -> list[float]:
        """Получает координаты страны (boundingbox)."""
        ...

    @abstractmethod
    def get_aeroplanes(self, country: str) -> list[list[Any]]:
        """Получает информацию о самолётах в воздушном пространстве страны."""
        ...


class AeroplanesAPI(BaseAPI):
    """Класс для работы с API nominatim и opensky."""

    NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
    OPENSKY_URL = "https://open-sky-network.org/api/states/all"

    def get_country_coordinates(self, country: str) -> list[float]:
        """Получает boundingbox страны через nominatim."""
        try:
            params: dict[str, str | int] = {
                "q": country,
                "format": "json",
                "limit": 1,
            }
            headers = {"User-Agent": "aeroplanes-coursework"}
            response = requests.get(
                self.NOMINATIM_URL, params=params, headers=headers, timeout=10
            )
            response.raise_for_status()
            data = response.json()
            if not data:
                return []
            return [float(x) for x in data[0]["boundingbox"]]
        except (requests.RequestException, ValueError, KeyError):
            return []

    def get_aeroplanes(self, country: str) -> list[list[Any]]:
        """Получает самолёты в воздушном пространстве страны."""
        bbox = self.get_country_coordinates(country)
        if not bbox:
            return []
        try:
            params: dict[str, float] = {
                "lamin": bbox[0],
                "lamax": bbox[1],
                "lomin": bbox[2],
                "lomax": bbox[3],
            }
            response = requests.get(
                self.OPENSKY_URL, params=params, timeout=10
            )
            response.raise_for_status()
            data = response.json()
            return data.get("states", []) or []
        except (requests.RequestException, ValueError):
            return []
