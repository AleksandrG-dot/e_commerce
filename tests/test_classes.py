# Тест класса Product
def test_product(first_product):
    assert first_product.name == "Aceline S201AMG"
    assert first_product.description == "Холодильник компактный белый"
    assert first_product.price == 10999.00
    assert first_product.quantity == 3


# Тест класса Category
def test_category(first_category, second_category):
    assert first_category.name == "Холодильники"
    assert first_category.description == "Устройства для охлаждения продуктов бытовые"
    assert len(first_category.products) == 2

    assert second_category.name == "Конвекторы"
    assert second_category.description == "Устройства для обогрева жилых помещений"
    assert len(second_category.products) == 3

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 5
    assert second_category.product_count == 5
