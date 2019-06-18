# is vs == in while
# Inheritance: IS A Relationship    | Generalization
# Maruti Suzuki Swift Dzire IS-A Swift
# Amazon eCommerce example
# Shoe, Mobile, LED Tv etc..... Objects
"""
class Shoe:
    def __init__(self,prodId,name,price,brand,color, size):
        self.prodId = prodId
        self.name = name
        self.price = price
        self.brand = brand
        self.color = color
        self.size = size

    def updateShowDetails(self,prodId,name,price,brand,color, size):
        self.prodId = prodId
        self.name = name
        self.price = price
        self.brand = brand
        self.color = color
        self.size = size

    def showShoeDetails(self):
        print("==== Shoe Details ====")
        print(self.prodId)
        print(self.name)
        print(self.price)
        print(self.brand)
        print(self.color)
        print(self.size)


class Mobile:
    def __init__(self, prodId, name, price, brand, ram, memory):
        self.prodId = prodId
        self.name = name
        self.price = price
        self.brand = brand
        self.ram = ram
        self.memory = memory

    def updateShowDetails(self, prodId, name, price, brand, ram, memory):
        self.prodId = prodId
        self.name = name
        self.price = price
        self.brand = brand
        self.ram = ram
        self.memory = memory

    def showShoeDetails(self):
        print("==== Mobile Details ====")
        print(self.prodId)
        print(self.name)
        print(self.price)
        print(self.brand)
        print(self.ram)
        print(self.memory)

class LEDTv:
    def __init__(self, prodId, name, price, brand, tech, screen):
        self.prodId = prodId
        self.name = name
        self.price = price
        self.brand = brand
        self.tech = tech
        self.screen = screen

    def updateShowDetails(self, prodId, name, price, brand, tech, screen):
        self.prodId = prodId
        self.name = name
        self.price = price
        self.brand = brand
        self.tech = tech
        self.screen = screen

    def showShoeDetails(self):
        print("==== LED Details ====")
        print(self.prodId)
        print(self.name)
        print(self.price)
        print(self.brand)
        print(self.tech)
        print(self.screen)





sRef = Shoe(101,"Alpha Bounce",8000,"Adidas","Black",9)
mRef = Mobile(105,"IPHONE",80000,"Apple",8,128)
lref = LEDTv(108,"Tru HD",89545,"Samsung","New","42")

sRef.showShoeDetails()
lref.showShoeDetails()
mRef.showShoeDetails()




"""



class Product:
    def __init__(self,prodID,price,name):
        self.name=name
        self.prodID = prodID
        self.price=price

    def updateProd(self,prodID,price,name):
        self.name = name
        self.prodID = prodID
        self.price = price

    def showProdDetails(self):
        print(self.name,self.prodID,self.price)

class Shoe(Product):
    def __init__(self,color,gend,type):
        self.color=color
        self.gend=gend
        self.type=type

    def showShoeDetails(self,color,gend,type):
        self.color = color
        self.gend = gend
        self.type = type


    def showShowDetails(self):
        print(self.color,self.gend,self.type)
