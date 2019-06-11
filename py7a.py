"""
    Object Oriented Programming Structure
    OOPS

    >OBJECT
    >Class


    > Encapsulation
    > Abstraction
    > Inheritance
    > Polymorphism

    Real World
    Object is anything which you can see and touch, anything which is real ==> Real time entity

    Class is drawing of an object
    Class is representation of how an object will look like
    What will you think of first??

    OOPS Principle
    1. Think of an object
    2. Draw Object
    3. Create real woobject by looking at drawing

    Computer Science:
    Object is a multi value container
            If we wish to customize multi value container we create objects
    Class is a textual representation of a object

    eg: Geometry Box
    All Pencils                         | Homogeneous
    pencil, eraser, sharpner            | Heterogeneous

    User is an object
    User has lot of data associated with it
        name
        phone
        email
        gender
        age
        address

    Identification of object
    Requirement
    User should register in my app
    enter src and dest location
    Book a cab
    User should be allocated a driver to complete drive

    Model View Controller Architectutre
    Model --> OBJECT
    Driver -- name, phone, mail, license, rating
    Cab --> brand, type, numberplate
    ride --> source, dest, cab, driver, user



    Ent
    Library system
    Requirements:
    Issue and return details
    User details
    book details
    Fine details
    Lender details

    Issue: Date of issue, time of issue, Lent by, borrowed by
    Return:Date of return, time of return,  lent to
    User: age, name, class, roll no, prev fine
    Book: name, author, edition, price, type
    Fine: gen book fine, text book, overnight issue, no of days for fine
    Lender details: ID, name,


"""


class User:
    pass


class Driver:
    pass


data = []
print(type(data))

# Object construction statement
u = User()
v = User()
d = Driver()
print(type(u))
print(type(d))

print(type(v))

print(u)
print(d)
print(v)


# Write Data in object
u.name = "John"
u.phone = "+91258978548"
u.email = "alsldas@falf.com"
u.address = "ABC Colony"

v.name = "as"
v.age = 59
v.salary = 7854

# Reference copy
w = v


d.name = "George"
d.phone = "5952688"
d.exp = "5"
d.lic = "ABD7868"

# Update operation in object
u.name = "John Watson"
v.age = "33"
print(v.age)
w.age= "44"
print(v.age)

# Delete operation
del u.phone
del d.lic

# Read operation
print(u.__dict__)
print(v.__dict__)
print(d.__dict__)

