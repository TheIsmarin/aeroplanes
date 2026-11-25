# Aeroplanes

Курсовой проект: интеграция с API самолётов (nominatim + opensky).

## Модули

### `src/api.py`
- `BaseAPI` — абстрактный класс для работы с API
- `AeroplanesAPI` — реализация для nominatim и opensky

### `src/aeroplane.py`
- `Aeroplane` — класс самолёта (позывной, страна, скорость, высота), сравнение по скорости и высоте, валидация

### `src/storage.py`
- `BaseStorage` — абстрактный класс для хранилища
- `JSONSaver` — сохранение в JSON

### `src/main.py`
- `user_interaction` — консольный интерфейс

## Установка

1. Клонируйте репозиторий:
```
git clone https://github.com/TheIsmarin/aeroplanes.git
```

2. Установите зависимости:
```
poetry install
```

## Использование

```
poetry run python -m src.main
```

## Тестирование

```
poetry run pytest
poetry run pytest --cov=src --cov-report=html
```

Покрытие: 99%

Отчёт покрытия: `htmlcov/index.html`