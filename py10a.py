class Parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print(">> Parent Constructor Executed")

    def showDetails(self):
        print("Hello", self.lname, self.fname)

class Child(Parent):            #IS-A
    def __init__(self,fname,lname,vehicle,salary):
        Parent.__init__(self,fname,lname)
        self.veh=vehicle
        self.sal=salary
        print(">> Child constructor executed")

    def showDetails(self):
        Parent.showDetails(self)
        print("Hello in child",self.veh,self.sal)

print("Parent class dict",Parent.__dict__)
print("Child class dict",Child.__dict__)

ch=Child("John","Watson",2,3000)
ch.fname="George"
ch.lname="Watson"
print(ch.__dict__)
print(Child.__dict__)
ch.showDetails()
Parent.showDetails(ch)
#Whatsover is in parent is accesible to child
