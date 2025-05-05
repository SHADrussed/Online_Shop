from unittest.mock import patch

from src.main import Product, Category, Smartphone, LawnGrass
import pytest

@pytest.fixture(autouse=True)
def reset_category_counts():
    """Сбрасывает счетчики категорий и продуктов перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0

@pytest.fixture
def product_phone():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

def test_init(product_phone):
    """Тест, что продукт корректно инициализируется с валидными входными данными."""
    assert product_phone.name == "Samsung Galaxy S23 Ultra"
    assert product_phone.description == "256GB, Серый цвет, 200MP камера"
    assert product_phone.price == 'Цена: 180000.0'
    assert product_phone.quantity == 5

@pytest.fixture
def product_none():
    return Product(None, "1024GB, Синий", 31000.0, 14)

def test_add():
    assert (Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
            + Product(None, "1024GB, Синий", 31000.0, 14) == 900000 + 31000 * 14)

def test_init2(product_none):
    """Тест, что продукт корректно инициализируется с именем None."""
    assert product_none.name is None
    assert product_none.description == "1024GB, Синий"
    assert product_none.price == 'Цена: 31000.0'
    assert product_none.quantity == 14

@pytest.fixture
def product_int():
    return Product("Наушники Picun", "12112324GB, Синd", 1999, 12)

def test_init3(product_int):
    """Тест, что продукт корректно инициализируется с целочисленной ценой."""
    assert product_int.name == "Наушники Picun"
    assert product_int.description == "12112324GB, Синd"
    assert product_int.price == 'Цена: 1999'
    assert product_int.quantity == 12

@pytest.fixture
def category_tv():
    return Category("Телевизоры",
                    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                    [Product("Наушники Picun", "12112324GB, Синd", 1999, 12)])

def test_category1(category_tv):
    """Тест, что категория корректно инициализируется с одним продуктом."""
    assert category_tv.name == "Телевизоры"
    assert category_tv.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert category_tv.products == """Наушники Picun, Цена: 1999 руб. Остаток: 12 шт.\n"""
    # assert category_tv.products[0].name == "Наушники Picun"
    # assert category_tv.products[0].description == "12112324GB, Синd"
    # assert category_tv.products[0].price == 'Цена: 1999'
    # assert category_tv.products[0].quantity == 12
    assert Category.category_count == 1
    assert Category.product_count == 1

def test_product_str(product_phone):
    """Тест, что метод __str__ возвращает правильное строковое представление продукта."""
    expected_str = 'Samsung Galaxy S23 Ultra, Цена: 180000.0 руб. Остаток: 5 шт.'
    assert str(product_phone) == expected_str

def test_product_str_none_name(product_none):
    """Тест, что метод __str__ корректно обрабатывает продукт с именем None."""
    expected_str = 'None, Цена: 31000.0 руб. Остаток: 14 шт.'
    assert str(product_none) == expected_str

def test_category_multiple_products():
    """Тест создания категории с несколькими продуктами и проверка счетчиков."""
    product1 = Product("Product1", "Desc1", 100.0, 10)
    product2 = Product("Product2", "Desc2", 200.0, 20)
    category = Category("TestCategory", "Test Description", [product1, product2])
    assert category.name == "TestCategory"
    assert category.description == "Test Description"
    # assert len(category.__products) == 2
    assert category.products == """Product1, Цена: 100.0 руб. Остаток: 10 шт.
Product2, Цена: 200.0 руб. Остаток: 20 шт.
"""
    # assert category.products[0].name == "Product1"
    # assert category.products[1].name == "Product2"
    assert Category.category_count == 1
    assert Category.product_count == 2

def test_multiple_categories():
    """Тест создания нескольких категорий и проверка общих счетчиков."""
    category1 = Category("Cat1", "Desc1", [Product("P1", "D1", 10.0, 1)])
    category2 = Category("Cat2", "Desc2", [Product("P2", "D2", 20.0, 2), Product("P3", "D3", 30.0, 3)])
    assert Category.category_count == 2
    assert Category.product_count == 3

def test_category_no_products():
    """Тест создания категории без продуктов."""
    category = Category("EmptyCategory", "No products here", [])
    assert category.name == "EmptyCategory"
    assert category.description == "No products here"
    assert len(category.products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product():
    """Тест задания 1, 2"""
    category = Category("Ураов", "Много спать пора", [Product("Собянин", 'Москву построил', 777, 1),
                        Product("Овощ", "Вкусный", 808080800, 213)])
    category.add_product(Product("Роблокс", "Удалила мне мама", 149, 999))
    assert """Собянин, Цена: 777 руб. Остаток: 1 шт.
Овощ, Цена: 808080800 руб. Остаток: 213 шт.
Роблокс, Цена: 149 руб. Остаток: 999 шт.
"""

def test_dictionary_convert():
    """Тест задания 3, конвертации"""
    product = {'name': "Альбом Lonerism", 'description': "Творчество Tame Impala", 'price': 18000, 'quantity': 32}
    actual = Product.new_product(product)
    expeted = Product("Альбом Lonerism", 'Творчество Tame Impala', 18000, 32)
    assert str(actual) == str(expeted)

def test_dictionary_convert_if_stance():
    """Тест задания 3, конвертации"""
    product = {'name': "Les Paul", 'description': "Офигенная гитара", 'price': 48000, 'quantity': 3}
    actual = Product.new_product(product, [Product("Овощ", "Вкусный", 808080800, 213),
                                           Product("Les Paul", "Офигенная гитара", 1231231, 4)])
    expeted = Product("Les Paul", "Офигенная гитара", 1231231, 7)
    assert str(actual) == str(expeted)

def test_price_change_exit():
    """Тест изменения цены в сеттере"""
    product = Product("Фрукт", "Невкуно", 231, 213)
    product.price = 0
    assert str(product) == str(Product("Фрукт", "Невкуно", 231, 213))

def test_price_change():
    """Тест изменения цены в сеттере, удачный"""
    product = Product("Фрукт", "Невкуно", 231, 213)
    product.price = 68970
    assert str(product) == str(Product("Фрукт", "Невкуно", 68970, 213))

@pytest.fixture
def product_for_price_test():
    """Фикстура для тестирования изменения цены."""
    return Product("Test Product", "Test Description", 1000.0, 10)

def test_price_decrease_confirmed(product_for_price_test):
    """Цена понижается после подтверждения 'y'."""
    with patch('builtins.input', return_value='y') as mock_input:
        product_for_price_test.price = 800.0
        mock_input.assert_called_once_with("Понизить цену товара на 200.0? (y/n): ")
        assert product_for_price_test.price == 'Цена: 800.0'

def test_price_decrease_declined(product_for_price_test):
    """Цена не понижается: 'n'."""
    with patch('builtins.input', return_value='n') as mock_input:
        product_for_price_test.price = 800.0
        mock_input.assert_called_once_with("Понизить цену товара на 200.0? (y/n): ")
        assert product_for_price_test.price == 'Цена: 1000.0'


#       ТЕСТЫ ФУНКЦИОНАЛА ИЗ 16.1, А ИМЕННО subclass of Product and __add__ of Product, also .append method check ones

# Фикстура для теста смартфона
@pytest.fixture
def smartphone_product():
    return Smartphone("Redmi note 8 pro", "ЛУчший, уже 6 лет держится", 18000.0, 4, 404, '8 pro', '64/128 GB', 'Black')
# Ну, без айфона никуда, для теста add
@pytest.fixture
def iphone_product():
    return Smartphone("IPhone 17", "Когда-нибудь выйдет", 119000, 1, 821, '17 MAX', '256/592 GB', 'Ion')

def test_smartphone_and_lawn_grass(smartphone_product):
    """Тесты на проверку создания подклассов"""
    lawn_product = LawnGrass("Трава", "Газончик, мой любимый. Ее обычно нехватает дотерам и тем, кто играет свип на гитаре", 119000, 1, 'Кризкистан', '1 год', 'red')
    assert str(lawn_product) == 'Трава, Цена: 119000 руб. Остаток: 1 шт.'
    assert str(smartphone_product) == 'Redmi note 8 pro, Цена: 18000.0 руб. Остаток: 4 шт.'


def test_new_add_in_product(smartphone_product, iphone_product):
    """Тест на __адд__ для продакт"""
    expected = 191000
    actual = smartphone_product + iphone_product
    assert expected == actual

# Ошибка в __адд__
def test_new_add_in_product_error(smartphone_product, product_for_price_test):
    """Тест на вызов ошибки в сложении, соответственно"""
    with pytest.raises(TypeError):
        smartphone_product + product_for_price_test

def test_append(category_tv, smartphone_product):
    """Тест на добавления товара в список и его ошибки"""
    with pytest.raises(TypeError):
        category_tv.add_product('фигня')
    category_tv.add_product(smartphone_product)