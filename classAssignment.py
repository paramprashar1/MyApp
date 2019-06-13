class Product:
    count = 0
    def __init__(self):
        Product.count +=1

    def showNumberofObjects(self):
        print("Total no. of objects:",Product.count)


p1 = Product()
p2 = Product()
p3 = Product()
p4 = p1
p5 = p3

p5.showNumberofObjects()
#Total Product Objects: