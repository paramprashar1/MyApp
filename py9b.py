class Order:

    def __init__(self,oid,price,restrauntName):
        self.oid = oid                          #Public
        self._price=price                       #Protected
        self.__restrauntName= restrauntName     #Private


    def showOrder(self):
        print(self.oid,self._price,self.__restrauntName)





o1=Order(101,3628,"ABC Masala")
# print(o1.__dict__)
# print(o1.oid)
#
# print(o1._price)
# #print(o1.__restrauntName)           #Cant be accessed directly
# print(o1._Order__restrauntName)
o1.showOrder()


#Sorting Algorithms : Geeks for Geeks

