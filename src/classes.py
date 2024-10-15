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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += str(product) + "\n"
            # result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" # Первонач. решение
        return result

    @property
    def products_list(self):
        return self.__products

    def __str__(self):
        count = 0
        for product in self.__products:
            count += product.quantity
        return f"{self.name}, количество продуктов: {count} шт."


class CategoryIterator:
    """Класс для итерации товаров в классе Category"""

    ctg: Category
    index: int

    def __init__(self, ctg_obj):
        self.ctg = ctg_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.ctg.products_list):
            product = self.ctg.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


class Smartphone(Product):
    """ Класс, содержащий смартфоны """
    efficiency: float   # производительность
    model: str          # модель
    memory: int         # объем встроенной памяти
    color: str          # цвет

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """ Класс, содержащий траву газонную """
    country: str                # страна-производитель
    germination_period: str     # срок прорастания
    color: str                  # цвет

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color