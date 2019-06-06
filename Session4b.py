technologies=["AI","Android","Hadoop","JEE"]
print(technologies)
technologies[1]="Mobile Applications"   #Update index 1
print(technologies)
del(technologies[1])
print(technologies)
print(technologies[1])
print(technologies[-1]) # minus signifies from the end index number
data=[10,20,30,40,50,"John","Jennie","Jim","Jack","Joe"]
data.pop(3)     #Removing index
print(data)
data.remove(data[3])    #Removing element
print(data)

names=["John","Jennie","Jim","Jack","Joe","John","Sia"]
names.remove("John")
print(names)

