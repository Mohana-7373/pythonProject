class shoppinglist:
    dict={"iphone":50000,"nokia": 5600,"samsung":18000,"realme":4000,"oppo":9000,"vivo":6000}
    cart={}
    def update_shoppinglist(self,itemname,value):
         self.dict[itemname] = value
         print(self.dict)
#shoplistObj = shoppinglist()
#shoplistObj.update_shoppinglist("vivo",6000)
    def update_cart(self,itemname,quantity):
        self.cart[itemname] = quantity
    def display_cart(self):
        for key, values in self.cart.items():
            print(key,values)
    def delete_cart(self,itemname):
        del self.cart[itemname]
    def total(self):
        for self.itemname in  self.dict:
            if self.itemname in self.cart:
                count=self.dict[self.itemname]*self.cart[self.itemname]
                print(count)


shoplistObj = shoppinglist()
shoplistObj.update_shoppinglist("vivo",6000)
shoplistObj.update_cart("oppo",2)
shoplistObj.update_cart("redmi",1)
shoplistObj.update_cart("hack",3)
shoplistObj.display_cart()
shoplistObj.delete_cart("hack")
shoplistObj.display_cart()
shoplistObj.total()


