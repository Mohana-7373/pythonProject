class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
    def display_Product_details(self):
        print(self.name)
        print(self.price)
        print(self.deal_price)
        print(self.rating)
class Electronic(Product):
    def __init__(self,warranty):
        self.warranty = warranty
    def get_warranty(self):
        print(self.warranty)
class Grocery(Product):
    def __init__(self,expiry_date,package_date):
        self.expiry_date = expiry_date
        self.package_date = package_date
    def get_expiry_date(self):
        print(self.expiry_date)

Obj = Product("T.V",40000,35000,3.5)
Obj.display_Product_details()
Obj1 = Grocery("4-5-2022","4-2-2022")
Obj1.get_expiry_date()
Obj2 = Electronic(3)
Obj2.get_warranty()


#super
class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
    def display_Product_details(self):
        print(self.name)
        print(self.price)
        print(self.deal_price)
        print(self.rating)
class Electronic(Product):
    def set_warranty(self,warranty):
        self.warranty = warranty
    def get_warranty(self):
        print(self.warranty)
class Grocery(Product):
    def __init__(self,name,price,deal_price,rating,expiry_date,package_date):
        super().__init__(name,price,deal_price,rating)
        self.expiry_date = expiry_date
        self.package_date = package_date
    def get_expiry_date(self):
        print(self.expiry_date)
class Order(Product):
    def __init__(self,order_type,order_address):
        items = {}
        self.order_type = order_type
        self.order_address = order_address
    def order_details(self):
        print(self.order_type)
        print(self.order_address)

Obj = Product("T.V",40000,35000,3.5)
Obj.display_Product_details()
Obj1 = Grocery("milk",30,25,4,2023,2025)
Obj1.get_expiry_date()
Obj2 = Electronic("Iphone",100000, 90000, 10)
Obj2.set_warranty(5)
Obj2.get_warranty()
Obj3 = Order("package_delivery","kdp")
Obj3.order_details()
