"""
Student
    name
    phone
    email
    password
    isCollegeTraining
    collegeName
    rollNum

"""
"""
class Student:
    pass
s1=Student()
s1.name="John"
s1.phone="+91 8595785644"
s1.email="john@example.com"
s1.password="pass123"
s1.isCollegeTrain=True
s1.collegeName="TIET"
s1.rollNum=22

print(s1.__dict__)

"""


class Student:

    schoolName="ATPL"
    # Self is a reference variable that holds hashcode of current object
    # __init__ is known as Constructor
    # Constructor is property of class
    def __init__(self,name,phone,email,password,isCollegeTraining,CollegeName,rollNum):
        self.name=name
        self.phone=phone
        self.email=email
        self.password=password
        self.isCollegeTraining=isCollegeTraining
        self.CollegeName=CollegeName
        self.rollNum=rollNum
        print(">>Self is",hex(id(self)))

    # Over Writing
    # def __init__(self,name,phone):
    #     self.name=name
    #     self.phone=phone


    def showStuDetails(self):
        print("=======================")
        print("Details of",self.name)
        print("Phone of",self.phone)
        print("Roll No",self.rollNum)
        print("=======================")


s1=Student("John","+91 885984550","asdasd@sf.com","affwe",True,"TIET","85745525851")
# print(">>s1 is",hex(id(s1)))
s2=Student("Fionna","+91 588664480058","asfwee33ewf@fs.com","dfsedge",False,"GNE","996349555")
# print(">>s2 is",hex(id(s2)))
# print("early s1",s1.__dict__)
# s1.vehicleNum="48885"
# s1.age="45"
#
# print("Later s1",s1.__dict__)
# print(s2.__dict__)


s1.showStuDetails()
s2.showStuDetails()
#We can do this in another way!
Student.showStuDetails(s1)
Student.showStuDetails(s2)
print()
print(s1.__dict__)
print(Student.__dict__)
print(s2.__dict__)

