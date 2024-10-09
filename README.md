# Электронный магазин каких-то объектов

## Модули
### - Модуль classes (описание классов)
- класс *Product(name, description, price, quantity)* - класс со свойствами: название, описание, цена и  
количество в наличии.
Альтернативный способ инициализации: new_product = Product.new_product({"name": "...", "description": "...", "price": ..., "quantity": })
- класс *Category(name, description, products)* - класс со свойствами: название, описание и список товаров  
категории. Имеет 2 атрибута класса: category_count - количество категорий и product_count - количество товаров.
Добавить товар - метод add_product(product)


## Зависимости и конфигурация
black==24.8.0
click==8.1.7
colorama==0.4.6
coverage==7.6.1
flake8==7.1.1
iniconfig==2.0.0
isort==5.13.2
mccabe==0.7.0
mypy==1.11.2
mypy-extensions==1.0.0
packaging==24.1
pathspec==0.12.1
platformdirs==4.3.6
pluggy==1.5.0
pycodestyle==2.12.1
pyflakes==3.2.0
pytest==8.3.3
pytest-cov==5.0.0
typing_extensions==4.12.2

## Инструкция по установке
Чтобы скачать репозиторий:  
`git clone https://github.com/AleksandrG-dot/e_commerce.git`

*Для установки зависимостей выполните команду:  
`pip install -r requirements.txt`

## Тестирование
- Модуль тестирования: pytest== 8.3.3  
- Количество тестов: 7
- Code coverage: 99%
