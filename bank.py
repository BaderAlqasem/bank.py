class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def showDetails(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)
        
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : $", self.balance)
        
    def withdraw(self, amount) :
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Balance Available : $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance : $", self.balance)
            
    def viewBalance(self):
        self.showDetails()
        print("Account balance: $", self.balance)
        
user = Bank("Bader", 20, "Male")
user.deposit(1000)
# user.viewBalance()
# user.showDetails()
user.withdraw(500)
user.viewBalance()
