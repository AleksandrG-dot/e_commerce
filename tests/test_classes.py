from unittest.mock import patch

import pytest

from src.classes import LawnGrass, Product, Smartphone


# Тест класса Product
def test_product(first_product):
    assert first_product.name == "Kitfort КТ-4104"
    assert first_product.description == "Холодильник косметический зеленый"
    assert first_product.price == 3699.00
    assert first_product.quantity == 6


# Тест класса Category
def test_category(first_category, second_category):
    assert first_category.name == "Холодильники"
    assert first_category.description == "Устройства для охлаждения продуктов бытовые"
    assert len(first_category.products_list) == 2

    assert second_category.name == "Конвекторы"
    assert second_category.description == "Устройства для обогрева жилых помещений"
    assert len(second_category.products_list) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5


# Тестирование альтернативного метода инициализации объекта класса Product
def test_product_new_poruct(product_new_product):
    assert product_new_product.name == "JBL Bar 9.1 черный"
    assert product_new_product.description == "Саундбар, 5.1.4, 820 Вт, 3D, Bluetooth, Wi-Fi, HDMI, HDMI, USB"
    assert product_new_product.price == 99999.00
    assert product_new_product.quantity == 1


# Тестирование сеттера цены price класса Product
def test_product_price_setter(capsys, product_new_product):
    # Изменяем цену на более высокую
    assert product_new_product.price == 99999
    product_new_product.price = 120000
    assert product_new_product.price == 120000

    # Изменяем цену на отрицательную (т.е. ошибка)
    product_new_product.price = -1000
    message = capsys.readouterr()
    assert (
        message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"
    )  # т.к. класс-миксин PrintMixin выводин 1 доп. строку
    assert product_new_product.price == 120000

    # Изменяем цену на 0 (т.е. ошибка)
    product_new_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product_new_product.price == 120000


# Тестирование сеттера цены price класса Product.
# Изменяем цену на меньшую, т.е. требуется подтверждение от пользователя
@patch("src.classes.input", return_value="y")
def test_product_price_setter_2(capsys, product_new_product):
    # Изменяем цену на меньшую чем была (требуется подтверждение)
    product_new_product.price = 10000
    assert product_new_product.price == 10000


# Тестирование строки с товарами класса Category
def test_category_product_property(first_category):
    assert (
        first_category.products
        == "Aceline S201AMG, 10999.0 руб. Остаток: 3 шт.\nIndesit ITS 4180 W, 32999.4 руб. Остаток: 2 шт.\n"
    )


# Тестирование метода добавления продукта в категорию
def test_category_add_product(first_category, first_product):
    assert len(first_category.products_list) == 2
    count_before = first_category.product_count
    first_category.add_product(first_product)
    assert len(first_category.products_list) == 3
    count_after = first_category.product_count
    assert count_after - count_before == 1


# Тестирование строкового представления класса Product (маг. метод __str__)
def test_product_str(first_product):
    assert str(first_product) == "Kitfort КТ-4104, 3699.0 руб. Остаток: 6 шт."


# Тестирование сложения проуктов класса Product (маг. метод __add__)
def test_product_add(first_product, product_new_product):
    assert first_product + product_new_product == (3699 * 6 + 99999 * 1)


# Тестирование строкового представления класса Category (маг. метод __str__)
def test_category_str(first_category):
    assert str(first_category) == "Холодильники, количество продуктов: 5 шт."


# Тестирование класса-итератора класса Category
def test_category_iterator(category_iterator):
    iter(category_iterator)
    assert category_iterator.index == 0
    assert next(category_iterator).name == "Aceline S201AMG"
    assert next(category_iterator).name == "Indesit ITS 4180 W"

    with pytest.raises(StopIteration):
        next(category_iterator)


# Тестирование создания объекта класса-наследника Smartphone
def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


# Тестирования функции сложения продуктов класса Smartphone
def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 2580000


# Тестирования функции сложения продуктов класса Smartphone - с ошибкой
def test_smartphone_add_error(smartphone1, LawnGrass1):
    with pytest.raises(TypeError):
        result = smartphone1 + 1
    with pytest.raises(TypeError):
        result = smartphone1 + LawnGrass1


# Тестирование создания объекта класса-наследника LawnGrass
def test_LawnGrass_init(LawnGrass1):
    assert LawnGrass1.name == "Газонная трава"
    assert LawnGrass1.description == "Элитная трава для газона"
    assert LawnGrass1.price == 500.0
    assert LawnGrass1.quantity == 20
    assert LawnGrass1.country == "Россия"
    assert LawnGrass1.germination_period == "7 дней"
    assert LawnGrass1.color == "Зеленый"


# Тестирования функции сложения продуктов класса LawnGrass
def test_LawnGrass_add(LawnGrass1, LawnGrass2):
    assert LawnGrass1 + LawnGrass2 == 16750


# Тестирования функции сложения продуктов класса LawnGrass - с ошибкой
def test_LawnGrass1_add_error(smartphone1, LawnGrass1):
    with pytest.raises(TypeError):
        result = LawnGrass1 + 1
    with pytest.raises(TypeError):
        result = LawnGrass1 + smartphone1


# Тестирование добавления в категорию не продукта - ошибка TypeError
def test_category_add_product_error(first_category):
    with pytest.raises(TypeError):
        first_category.add_product("Any text or data")


# Тестирование класс-миксина PrintMixin (выводит в консоль инфу о создаваемом экземпляре)
def test_printmixin(capsys):
    Product("Kitfort КТ-4104", "Холодильник косметический зеленый", 3699.00, 6)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Kitfort КТ-4104, Холодильник косметический зеленый, 3699.0, 6)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"


# Тестирование попытки создания товара с нулевым количеством
def test_product_zero_quantiti():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


# Тестирование метода подсчета средней стоимости товаров в категории middle_price
def test_category_middle_price(second_category, category_without_product):
    assert second_category.middle_price() == 10999.33
    assert category_without_product.middle_price() == 0
