quote = "Work hard and get luckier"
"""
data1 = list(quote)   #Converting string to list
print(data1,type(data1))
data2=tuple(quote)
data3=set(quote)
print(data2,type(data2))
print(data3,type(data3))

print(quote*2)
print(quote[::-1])
"""
for i in range(len(quote)-1, -1, -1):
    print(quote[i], end=" ")

