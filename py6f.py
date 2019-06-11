#Variable Arguments
def addNumbers(*args):
    print(args)
    print(type(args))

    sum=0
    for elm in args:
        sum+=elm

    print(sum)

addNumbers(10,20,30,40,50)
addNumbers(10,20)
addNumbers(10)


