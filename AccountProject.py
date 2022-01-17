class Bank():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = 0
        
    def showDetails(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)
    
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
        
Bader = Bank("Bader", 20, "Male")
Bader.deposit(1000)
Bader.viewBalance()
Bader.withdraw(800)

Jane = Bank("Jane", 29, "Female")
Jane.deposit(500)
Jane.viewBalance()
Jane.withdraw(499)