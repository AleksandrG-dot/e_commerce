""" Модуль с описанием классов, используемых в проекте """


class Product:
    """Класс для представления продукции"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict):
        return cls(**product_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            answer = input(f"Цена понижается с {self.__price} по {new_price}. Подтвержаете? (y/n)")
            if answer == "y":
                self.__price = new_price
        else:
            self.__price = new_price


class Category:
    """Класс для представления категорий с продукцией"""

    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    @property
    def products_list(self):
        return self.__products
