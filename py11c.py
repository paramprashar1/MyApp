#class CA():
#class CA:
#Any class made in pyhton is child of object
class CA(object):
    pass

class CB(CA):
    pass
cRef = CA()
print("Object data",cRef.__dict__)
print("Class data",CA.__dict__)
print("Class data",CB.__dict__)
