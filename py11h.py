class Order:

    def __init__(self,oid,CustomerName,dishCount,price):
        self.oid=oid
        self.CustomerName=CustomerName
        self.dishCount=dishCount
        self.price=price

    def toCSV(self):
        return "{}, {}, {}\n".format(self.oid,self.CustomerName,self.dishCount,self.price)




o1=Order(1,"John",5,500)
o2=Order(2,"Jennie",55,780)
o3=Order(3,"Jim",785,985)

# print(o1.__dict__)
# print(o2.__dict__)
# print(o3.__dict__)
print(o1.toCSV())
print(o2.toCSV())
print(o3.toCSV())


#Persistance : Store/Save the data of an object somewhere
#1 Files
#2 Database --> SQL, no SQL

file = open("G:\TV Series\Friends\Season 01\MyApp.csv","a")
file.write(o1.toCSV())
file.write(o2.toCSV())
file.write(o3.toCSV())

print("Orders Saved")