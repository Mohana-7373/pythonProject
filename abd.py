milk = GroceryItem("Milk",40,25,3.5)
tv = ElectronicItem("Tv",45000,40000,3.5)
order = Order("Prime Delivery","hyd")
order.add_item(milk,2)
order.add_item(tv,1)
print("+++++")
order.display_order_details()
print("++++++")
order.display_total_bill()