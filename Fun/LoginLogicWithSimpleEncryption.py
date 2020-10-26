
class User:
    def __init__(self,name,password):
        self.name= name
        self.password = self.encryptPassword(password)
        # print(self.password)
    def login(self,name,password):
        if(name == "" or password==""):
            print("Please provide your creditianls to proceed")
            return
        a = self.decryptPassword(password)
        # print(a)
        if(name==self.name and password==a):
            print("Valid Input")
            self._welcome()
        else:
            print("Invalid Input")
    def _welcome(self):
        print("Hey "+self.name )
        print("We will start a game")
    def encryptPassword(self,password):
        passwA=[]
        for i in password:
            passwA.append(chr(ord(i)+2))
        return "".join(passwA)
    def decryptPassword(self,password):
        passwD=[]
        for i in self.password:
            passwD.append(chr(ord(i)-2))
        return "".join(passwD)

        
user1 = User("vaibhav","soni")
user1.login("vaibhav","soni")
# user1._welcome()
        
