"""
    Relationship Mapping

        HAS A MAPPING

        1 Engineer working on 1 Project
        1 Engineer working on many projects
        Many engineers working on mnay projects

        1 CUSTOMER HAS 1 ADDRESS
        1 CUSTOMER HAS MANY ADDRESSES
        MANY CUSTOMERS HAVE MANY CUSTOMERS

    1 DOCTOR WORKING ON 1 PATIENT
    1 DOCTOR WORKING ON MANY PATIENTS
    MANY DOCTOR WORKING ON MANY PATIENTS




    Customer
        name
        phone
        email

    Address
        adrsLine
        city
        state

    Doctor
        Name
        Phone
        Department
    Patient
        Name
        Age
        Ailment

class Customer:




"""

class Address:
    #Constructor for standardization
    def __init__(self,addressLine,city,state):
        self.addressLine=addressLine
        self.city=city
        self.state=state

    def updateCustomerDetails(self,addressLine,city,state):
        self.addressLine = addressLine
        self.city = city
        self.state = state

    def showCustomerDetails(self):
        print("===================")
        print("Address:\t",self.addressLine)
        print("City:\t", self.city)
        print("State:\t", self.state)
        print("===================")

    def __del__(self):
        print("This is optional as per requirement")


class Customer:
    # Constructor for standardization
    def __init__(self, name, phone, email,addresses):
        self.name = name
        self.phone = phone
        self.email = email
        self.addresses=addresses

    def updateCustomerDetails(self, name, phone, email,addresses):
        self.name = name
        self.phone = phone
        self.email = email
        self.addresses=addresses

    def showCustomerDetails(self):
        print("===================")
        print("Name:\t", self.name)
        print("Email:\t", self.email)
        print("Ph No:\t", self.phone)
        print("Addresses:\t")
       # self.addresses.showCustomerDetails()
        for adrs in adrsList:
            adrs.showCustomerDetails()
        print("===================")

    def __del__(self):
        print("This is optional as per requirement")


# c1=Customer("John","+91 85468522","john@example.com")
# a1=Address("Redwood Shores","Bangalore","Karnataka")
a1=Address(None,None,None)
a1.addressLine=input()
a1.city=input()
a1.state=input()

a2=Address("Civil Lines","Ludhiana","Punjab")

#List of Addresses

adrsList = [a1,a2]
c1=Customer("John","+91 85468522","john@example.com",adrsList)

#c1.showCustomerDetails()
# a1.showCustomerDetails()
# a2.showCustomerDetails()

cRef=c1
cRef.showCustomerDetails()










"""
    One order can have many food items
    WithUser Input create a small program
    add as many as FoodItems in the list called cart
    create a function in order --> getTotalAmount() which returns total
    Create a function apply promoCode in order class which returns a discounted price
    


"""

