# Logic by which problem is solved
"""
1 Operators
2 conditional constructs
3 loops/ iterations
"""


#Arithmetic operators + ,- ,*, / ,// ,**
dish1=100
dish2=200
bill=dish1+dish2

print("Bill is", bill)

#assume tax to be 5%

taxes=0.05*bill
print("taxes:",taxes)

tbill=bill+taxes
print("Total Bill",tbill)
#multiplication
num1=2
num2=3
num3=num1*num2
print(num3)
#exponent
numa=3
numb=2
numc=numa**numb
print(numc)

#divide
numa=3
numb=2
numc=numa/numb
print(numc)

# double divide integral value only

numa=3
numb=2
numc=numa//numb
print(numc)

#Modulus operator % remainder only
numa=10
numb=2
numc=numa%numb
print(numc)

#last two digits extracted
number=249
data=number%100
print(data)

# Hundreds place extracted
data2=number//100
print(data2)

# HW : Add digits of a number


