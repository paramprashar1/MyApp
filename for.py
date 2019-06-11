n=int(input("Enter your number"))
if n>=1 and n<101:
    if n%2 is not 0:
        print("Weird")
    elif n%2 is 0 and n>=2 and n<=5:
        print("Not Wierd")
    elif n%2 is 0 and n>=6 and n<=20:
        print("Weird")
    elif n%2 is 0 and n>20:
        print("Not Weird")


