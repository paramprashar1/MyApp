class Product:

    restaurantName = "ABC"

    #Constructor
    #Hard Code
    # def __init__(self):
    #     self.name="Dal Makhni"
    #     self.price="200"

    #Dynamic
    def __init__(self,name,price):
        self.name=name
        self.price=price

    #Function
    def showProduct(self):
        print(self.name,self.price,Product.restaurantName)

    #Destructor
    def __del__(self):
        print("Product deleted")



p1=Product("Paneer","200")
p2=Product("Chicken","500")

print(p1.__dict__)
print(p2.__dict__)

p1.showProduct()
p2.showProduct()

print(id(p1))
print(id(p2))
del p1
print("Thank you")
