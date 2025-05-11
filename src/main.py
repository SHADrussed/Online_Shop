from abc import ABC, abstractmethod


class BaseProduct:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def new_product(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

class MixinLog:
    def __init__(self):
        print(f'{self.__class__.__name__}({self.name}, {self.description}, {self._Product__price}, {self.quantity})')


class Product(BaseProduct, MixinLog):
    name: str
    description: str
    _price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        if not quantity:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'
    @property
    def price(self):
        return f'Цена: {self._price}'

    @price.setter
    def price(self, new_value):
        if new_value <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            if new_value < self._price:
                user_answer = input(f"Понизить цену товара на {self._price - new_value}? (y/n): ")
                if user_answer == 'y':
                    self._price = new_value
            else:
                self._price = new_value


    @classmethod
    def new_product(cls, data: dict, products: list = None):
        name, description, price, quantity = data.get('name'), data.get('description'), data.get('price'), data.get('quantity')
        if products:
            for product in products:
                if product.name == name:
                    product.quantity += quantity
                    if price > product._price:
                        product._price = price
                    return product
        new_product = cls(name, description, price, quantity)

        if products is not None:
            products.append(new_product)

        return new_product
    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать разные классы продуктов")
        return self.quantity * self._price + other.quantity * other._price


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class BaseCategoryOrder:
    @abstractmethod
    def __init__(self):
        pass

class Category(BaseCategoryOrder):
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        if not isinstance(product, Product) or not issubclass(type(product), Product):
            raise TypeError("Можно добавить только объекты класса Product и его подклассов")
        self.__products.append(product)
        Category.category_count += 1

    @property
    def products(self):
        product_output = ''
        for product in self.__products:
            product_output += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return product_output

    def __str__(self):
        return f'{self.name}, количество продуктов: {sum([i.quantity for i in self.__products])} шт.'

    def __iter__(self):
        self.starting_point = -1
        return self

    def __next__(self):
        if self.starting_point + 1 < len(self.__products):
            self.starting_point += 1
            return self.__products[self.starting_point]
        else:
            StopIteration

    def average_pricetag(self):
        try:
            total = sum(p._price for p in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0.0



class Order(BaseCategoryOrder):
    product: str
    quantity: int
    total: float

    def __init__(self, product, quantity, total):
        self.product = product
        self.quantity = quantity
        self.total = total

    def product(self):
        return f'Продукт: {self.product}'

    def quantity(self):
        return f'Количество: {self.quantity} шт.'

    def total(self):
        return f'Полная цена: {self.total} руб.'


