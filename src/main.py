"""Демонстрация работы с API самолётов."""

from src.aeroplane import Aeroplane
from src.api import AeroplanesAPI
from src.storage import JSONSaver


def user_interaction() -> None:
    """Взаимодействие с пользователем."""
    api = AeroplanesAPI()
    saver = JSONSaver()

    country = input("Введите название страны: ").strip()
    print(f"Получаем самолёты для страны: {country}")

    raw = api.get_aeroplanes(country)
    aeroplanes = Aeroplane.cast_to_object_list(raw)
    print(f"Найдено самолётов: {len(aeroplanes)}")

    if not aeroplanes:
        print("Самолётов не найдено.")
        return

    top_n = int(input("Введите количество самолётов для топ N по высоте: "))
    top = sorted(aeroplanes, key=lambda a: a.altitude, reverse=True)[:top_n]
    print("\nТоп по высоте:")
    for a in top:
        print(a)

    filter_country = input(
        "Введите страну регистрации для фильтрации (или Enter): "
    ).strip()
    if filter_country:
        filtered = [a for a in aeroplanes if a.country == filter_country]
        print(f"\nСамолёты из {filter_country}:")
        for a in filtered:
            print(a)

    for a in top:
        saver.add_aeroplane(a)
    print("\nДанные сохранены в aeroplanes.json")


if __name__ == "__main__":
    user_interaction()
