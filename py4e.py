#Cart is an empty list with len as 0
"""
cart=["Chicken"]
cart.append("Dal Makhni")
cart.append("Paneer Butter Masala")
print(cart)

cart.extend(["Noodles","Manchurian"])
print(cart)

cart.insert(1,"Soya Champ")
print(cart)
cart.pop(2)
print(cart)
print(cart[2])
"""

cart=[]
choice="yes"
while choice=="yes" or choice=="Yes":
    foodItem=input("Add Food Item in Cart")
    cart.append(foodItem)
    choice=input("Would you like to add more Items?, yes or no?")
print(cart)
print("Thank you you've added",len(cart),"items")