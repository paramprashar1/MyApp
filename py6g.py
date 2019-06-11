# Keyword Arguments
def marks(**kwargs):
    print(kwargs)
    print(type(kwargs))

marks(physics=90, maths=92, chemistry=90)
#Key has to be string cant be variable

def fun(*a,**b):
    print(a)
    print(b)

fun(10,20,30,40,50,a=10,b=50,c=588)
