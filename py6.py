# Functions
"""
f(x) = x*x
f(2)= 2*2 -> 4

Functions in programming language -> Methods/ Procedures/ Routines
    Function is instructions which should be executed in a sequence
    Why loops?
    So we can perform certain tasks again an again
    Why Functions?
    They can also be executed again and again but they represent some task to be done again and again

    Functions provide modularity
    Modularization:
    registerUser =

    1_Functions have a suitable name
    Eg: registerUser
    2_It may or may not have inputs
    3_It will have definition
    4_It may or may not have acknowledgement


"""
sender = "85985612314"
senderBalance = 10000
receiver = "9915517777"
receiverBalance = 5000
amt = 500
"""

senderBalance -= amt
receiverBalance += amt
print("New receiver Balance",receiverBalance)
print("New Sender Balance",senderBalance)
"""


def pay(sender, receiver, amt,):
    print(sender, "has sent", amt,"to", receiver)

pay("54878","5985",500)


def addNumb(num1,num2):
    num3 = num1+num2
    print(num1,"+",num2,"=",num3)

addNumb(10,20)
