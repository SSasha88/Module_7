print('Задача "Учёт товаров"')
print()
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        content = file.read().strip()
        file.close()
        if not content:
            return ""
        return content
    def add(self, *products):
        existing_products = set(self.get_products().split('\n'))
        file = open(self.__file_name, 'a')
        for product in products:
            product_str = str(product)
            if product_str in existing_products:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                file.write(product_str + "\n")
                existing_products.add(product_str)
        file.close()


#Пример результата выполнения программы:
#Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())