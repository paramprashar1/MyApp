data=[1,2,3,4,5]
length=len(data)
print(length)
print(len(data))
print(max(data))
print(min(data))

#Max nd min dont work in heterogenous containers

names=["John","Annie","Bob","George","Kia","Krish"]
print(max(names))
print(min(names))
#Max and min are determined alphabetically

print("==========")
for i in range(0,len(names),2):
    print(names[i])

print("=======")
#Enhanced for each READ ONLY loop
for name in names:
    print(name)

