from src.main import Product, Category
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
    assert product_phone.price == 180000.0
    assert product_phone.quantity == 5

@pytest.fixture
def product_none():
    return Product(None, "1024GB, Синий", 31000.0, 14)

def test_init2(product_none):
    """Тест, что продукт корректно инициализируется с именем None."""
    assert product_none.name is None
    assert product_none.description == "1024GB, Синий"
    assert product_none.price == 31000.0
    assert product_none.quantity == 14

@pytest.fixture
def product_int():
    return Product("Наушники Picun", "12112324GB, Синd", 1999, 12)

def test_init3(product_int):
    """Тест, что продукт корректно инициализируется с целочисленной ценой."""
    assert product_int.name == "Наушники Picun"
    assert product_int.description == "12112324GB, Синd"
    assert product_int.price == 1999
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
    assert category_tv.products[0].name == "Наушники Picun"
    assert category_tv.products[0].description == "12112324GB, Синd"
    assert category_tv.products[0].price == 1999
    assert category_tv.products[0].quantity == 12
    assert Category.category_count == 1
    assert Category.product_count == 1

def test_product_str(product_phone):
    """Тест, что метод __str__ возвращает правильное строковое представление продукта."""
    expected_str = "Product(name=Samsung Galaxy S23 Ultra, description=256GB, Серый цвет, 200MP камера, price=180000.0, quantity=5)"
    assert str(product_phone) == expected_str

def test_product_str_none_name(product_none):
    """Тест, что метод __str__ корректно обрабатывает продукт с именем None."""
    expected_str = "Product(name=None, description=1024GB, Синий, price=31000.0, quantity=14)"
    assert str(product_none) == expected_str

def test_category_multiple_products():
    """Тест создания категории с несколькими продуктами и проверка счетчиков."""
    product1 = Product("Product1", "Desc1", 100.0, 10)
    product2 = Product("Product2", "Desc2", 200.0, 20)
    category = Category("TestCategory", "Test Description", [product1, product2])
    assert category.name == "TestCategory"
    assert category.description == "Test Description"
    assert len(category.products) == 2
    assert category.products[0].name == "Product1"
    assert category.products[1].name == "Product2"
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