#Pass by reference

def squareOfNum(nums):
    for i in range(0,len(nums)):
        nums[i]=nums[i]*nums[i]

numbers=[1,2,3,4,5]
squareOfNum(numbers)
print(numbers)

def fun(a,b,c):
    pass

fun(a=10,b=20,c=30)

