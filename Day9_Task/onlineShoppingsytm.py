# Online Shopping System (Multilevel Inheritance) 

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, brand, storage):
        super().__init__(name, price, brand)
        self.storage = storage

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Storage:", self.storage)

m = MobilePhone("Smartphone", 20000, "Samsung", "128GB")
m.display()