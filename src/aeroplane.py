"""Модуль с классом Aeroplane."""


class Aeroplane:
    """Класс для представления самолёта."""

    callsign: str
    country: str
    speed: float
    altitude: float

    def __init__(self, callsign: str, country: str, speed: float, altitude: float) -> None:
        """Инициализация самолёта с валидацией."""
        if not callsign or not isinstance(callsign, str):
            raise ValueError("Некорректный позывной")
        if not country or not isinstance(country, str):
            raise ValueError("Некорректная страна регистрации")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        if altitude < 0:
            raise ValueError("Высота не может быть отрицательной")

        self.callsign = callsign
        self.country = country
        self.speed = speed
        self.altitude = altitude

    def __str__(self) -> str:
        """Строковое отображение."""
        return f"{self.callsign}, {self.country}, " f"скорость: {self.speed} м/с, высота: {self.altitude} м"

    def __lt__(self, other: "Aeroplane") -> bool:
        """Сравнение по скорости."""
        return self.speed < other.speed

    def __gt__(self, other: "Aeroplane") -> bool:
        """Сравнение по высоте."""
        return self.altitude > other.altitude

    def __eq__(self, other: object) -> bool:
        """Сравнение по скорости и высоте."""
        if not isinstance(other, Aeroplane):
            return NotImplemented
        return self.speed == other.speed and self.altitude == other.altitude

    @classmethod
    def cast_to_object_list(cls, data: list[list]) -> list["Aeroplane"]:
        """Преобразует список списков из API в список объектов Aeroplane."""
        result = []
        for item in data:
            try:
                callsign = (item[1] or "").strip()
                country = item[2] or ""
                speed = item[9] or 0
                altitude = item[13] or 0
                if callsign and country:
                    result.append(cls(callsign, country, float(speed), float(altitude)))
            except (IndexError, ValueError, TypeError):
                continue
        return result
