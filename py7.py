# Local and Global Variables



num=10

def show():
    num = 11
    print(">>1, num is",num)        #Local
show()
print(">>2, num is:",num)           #Global


def show():
    global num
    num = num%3
    print(">>3, num is",num)        #Global

show()
print(">>4, num is:",num)           #Global

cart=[]

def addProductToCart(product):

    global cart

    cart.append(product)

