class Login:

    def loginUser(self):
        print(">> Login dear User")

class GoogleLogin(Login):
    def loginUser(self,email,password):
        print(">> Google login Done")

class otpLogin(Login):
    def loginUser(self,phone):
        print(">> OTP Login done")

class fbLogin(Login):
    def loginUser(self,fbUsern,passw):
        print("FB Login done!")

class Cab:
    def bookCab(self,source,destination):
        print(">> Cab order from {} to {}".format(source,destination))

class OLAMicro(Cab):
    def bookCab(self,source,destination):
        print(">> Cab order from {} to {}".format(source,destination))

class OLAMini(Cab):
    def bookCab(self,source,destination):
        print(">> Cab order from {} to {}".format(source,destination))

class OLASedan(Cab):
    def bookCab(self,source,destination):
        print(">> Cab order from {} to {}".format(source,destination))

# In Python everything is RUNTIME
# Runtime Polymorphism
login=Login()
login.loginUser()

print()
login = GoogleLogin()
login.loginUser("john@example.com","pass123")
print()
login = otpLogin()
login.loginUser("123456")
print()


cab = Cab()
cab.bookCab("Silver arc", "MBD")

print()

cab = OLASedan()
cab.bookCab("Kitchlu Ngr","SHCS")