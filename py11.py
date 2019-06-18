class Customer:
    def __init__(self,name,membership,account):
        self.name = name

        #Dependance --> Coupling
        self.account = account          #Has A
        self.membership = membership    #Has A


#HAS A
class Membership:
    pass

class Regular(Membership):
    pass

class Prime(Membership):
    pass


#IS A
class BankAccount:
    pass

class SavingsAc(BankAccount):
    pass

class CurrentAc(BankAccount):
    pass

mShip = Regular()
account = SavingsAc()

cRef = Customer("John",mShip,account)
