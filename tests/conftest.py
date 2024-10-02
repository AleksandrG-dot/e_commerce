import pytest

from src.classes import Category, Product


@pytest.fixture
def first_product():
    return Product("Aceline S201AMG", "Холодильник компактный белый", 10999.00, 3)


@pytest.fixture
def first_category():
    return Category(
        name="Холодильники",
        description="Устройства для охлаждения продуктов бытовые",
        products=[
            Product("Aceline S201AMG", "Холодильник компактный белый", 10999.00, 3),
            Product("Indesit ITS 4180 W", "Холодильник с морозильником белый", 32999.40, 2),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Конвекторы",
        description="Устройства для обогрева жилых помещений",
        products=[
            Product("Aceline CV-2000SWYL", "Холодильник компактный белый", 10999.00, 5),
            Product("Xiaomi Mi Smart Space Heater S", "Конвектор 2200 Вт, 20 м², Wi-Fi", 9999.99, 2),
            Product(
                "Ballu Plaza Solar BIHP/S-1300",
                "Конвективно-инфракрасный обогреватель 1300 Вт, 15 м², дисплей, регулировка мощности",
                11999,
                1,
            ),
        ],
    )
