"""Модуль для работы с хранилищем самолётов."""

import json
from abc import ABC, abstractmethod
from typing import Any

from src.aeroplane import Aeroplane


class BaseStorage(ABC):
    """Абстрактный класс для работы с хранилищем."""

    @abstractmethod
    def add_aeroplane(self, aeroplane: Aeroplane) -> None:
        """Добавляет самолёт в хранилище."""
        ...

    @abstractmethod
    def delete_aeroplane(self, aeroplane: Aeroplane) -> None:
        """Удаляет самолёт из хранилища."""
        ...

    @abstractmethod
    def get_aeroplanes(self, criteria: dict[str, Any]) -> list[dict[str, Any]]:
        """Получает самолёты по критериям."""
        ...


class JSONSaver(BaseStorage):
    """Класс для сохранения самолётов в JSON-файл."""

    def __init__(self, filename: str = "aeroplanes.json") -> None:
        """Инициализация с именем файла."""
        self.filename = filename

    def add_aeroplane(self, aeroplane: Aeroplane) -> None:
        """Добавляет самолёт в JSON."""
        data = self._load()
        data.append(
            {
                "callsign": aeroplane.callsign,
                "country": aeroplane.country,
                "speed": aeroplane.speed,
                "altitude": aeroplane.altitude,
            }
        )
        self._save(data)

    def delete_aeroplane(self, aeroplane: Aeroplane) -> None:
        """Удаляет самолёт из JSON."""
        data = self._load()
        data = [
            item
            for item in data
            if not (
                item["callsign"] == aeroplane.callsign
                and item["country"] == aeroplane.country
            )
        ]
        self._save(data)

    def get_aeroplanes(self, criteria: dict[str, Any]) -> list[dict[str, Any]]:
        """Возвращает самолёты по критериям (заглушка для БД)."""
        data = self._load()
        result: list[dict[str, Any]] = []
        for item in data:
            if all(item.get(k) == v for k, v in criteria.items()):
                result.append(item)
        return result

    def _load(self) -> list[dict[str, Any]]:
        """Загружает данные из файла."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data: list[dict[str, Any]] = json.load(f)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save(self, data: list[dict[str, Any]]) -> None:
        """Сохраняет данные в файл."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
