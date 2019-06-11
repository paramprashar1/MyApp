def addNumbers(num1, num2):
    sum = num1 + num2
    print("Sum is", sum)

def addNos(num1, num2):
    sum = num1 + num2
    return sum

addNumbers(10,20)
print("Sum of 30 and  40 is:", addNos(30,40))
result=addNos(20,30)
if result>30:
    print("pass")
else:
    print("fail")

print(addNumbers(10,20))
print(addNos(20,30))

def hello(name):
    print("Hello", name)

hello("John")
print("hello is", hello)

hi = hello
print("Hi is ", hi)

hi("Fionna")


