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
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product_new_product.price == 120000

    # Изменяем цену на 0 (т.е. ошибка)
    product_new_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product_new_product.price == 120000

    # # Изменяем цену на меньшую чем была (требуется подтверждение)
    # product_new_product.price = 1000
    # message = capsys.readouterr()
    # assert message.out.strip() == 'Цена понижается с 120000 по 1000. Подтвержаете? (y/n)'
    # # Не знаю как передать в консоль 'y' или 'n'
    # assert product_new_product.price == 120000


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
