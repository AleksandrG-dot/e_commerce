import pytest

from src.classes import Category, CategoryIterator, LawnGrass, Product, Smartphone


@pytest.fixture
def first_product():
    return Product("Kitfort КТ-4104", "Холодильник косметический зеленый", 3699.00, 6)


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


@pytest.fixture
def product_new_product():
    return Product.new_product(
        {
            "name": "JBL Bar 9.1 черный",
            "description": "Саундбар, 5.1.4, 820 Вт, 3D, Bluetooth, Wi-Fi, HDMI, HDMI, USB",
            "price": 99999.0,
            "quantity": 1,
        }
    )


@pytest.fixture
def category_iterator(first_category):
    return CategoryIterator(first_category)


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def LawnGrass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def LawnGrass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
