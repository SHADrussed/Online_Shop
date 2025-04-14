class Product:
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
        return f"Product(name={self.name}, description={self.description}, price={self.__price}, quantity={self.quantity})"
    @property
    def price(self):
        return f'Цена: {self.__price}'

    @price.setter
    def price(self, new_value):
        if new_value <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            if new_value < self.__price:
                user_answer = input(f"Понизить цену товара на {self.__price - new_value}? (y/n): ")
                if user_answer == 'y':
                    self.__price = new_value
            else:
                self.__price = new_value


    @classmethod
    def new_product(cls, data: dict, products: list = None):
        name, description, price, quantity = data.get('name'), data.get('description'), data.get('price'), data.get('quantity')
        if products:
            for product in products:
                if product.name == name:
                    product.quantity += quantity
                    if price > product.__price:
                        product.__price = price
                    return product
        new_product = cls(name, description, price, quantity)

        if products is not None:
            products.append(new_product)

        return new_product

class Category:
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
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объекты класса Product")
        self.__products.append(product)
        Category.category_count += 1

    @property
    def products(self):
        product_output = ''
        for product in self.__products:
            product_output += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return product_output



# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#
#     print(product2.name)
#     print(product2.description)
#     print(product2.price)
#     print(product2.quantity)
#
#     print(product3.name)
#     print(product3.description)
#     print(product3.price)
#     print(product3.quantity)
#
#     category1 = Category("Смартфоны",
#                          "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#                          [product1, product2, product3])
#
#     print(category1.name == "Смартфоны")
#     print(category1.description)
#     #print(len(category1.products))
#     print(category1.category_count)
#     print(category1.product_count)
#
#     product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#     category2 = Category("Телевизоры",
#                          "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#                          [product4])
#
#     print(category2.name)
#     print(category2.description)
#     #print(len(category2.products))
#     #print(category2.products)
#
#     print(Category.category_count)
#     print(Category.product_count)
#
#     product4 = Product(None, "1024GB, Синий", 31000.0, 14)
#     print(product4)
#     new = Category("Телевизоры",
#                     "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#                     [Product("Наушники Picun", "12112324GB, Синd", 1999, 12)])
#     print(new.products)
#
#     category = Category("Ураов", "Много спать пора", [Product("Собянин", 'Москву построил', 777, 1),
#                                                       Product("Овощ", "Вкусный", 808080800, 213)])
#     category.add_product(Product("Роблокс", "Удалила мне мама", 149, 999))
#     print(category.products)