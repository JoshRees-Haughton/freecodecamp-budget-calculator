class Category:
    ledger = []
    balance = 0
    
    def __init__(self, name):
        #When initialised, the name of the category is input
        self.name = name

    def deposit(self, amount, description = ''):
        self.deposit_info = {'amount': amount, 'description': description}
        self.ledger.append(self.deposit_info)
        #print(self.ledger)
        self.balance += amount
        #print(self.balance)
    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.withdraw_info = {'amount': -amount, 'description': description}
            self.ledger.append(self.withdraw_info)            
            self.balance -= amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance
        
    def transfer(self, amount, category):
        if self.balance >= amount:
            self.withdraw(amount, "Transfer to {}".format(category.name))
            category.deposit(amount, "Transfer from {}".format(self.name))
            return True
        else:
            return False
    
    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True
        
    def create_spend_chart(categories):
        pass


#class Person:
#  def __init__(self, name, age):
#    self.name = name
#    self.age = age


Food = Category("Food")
Fun = Category("Fun")


print("Balance ok")
print("**********")
print("")

print("Deposit 12 into Food")
Food.deposit(12, "test")
print("Food balance: " + str(Food.get_balance()))
print("Fun balance: " + str(Fun.get_balance()))
print("")

print("Deposit 11 into Fun")
Fun.deposit(11, "test")
print("Food balance: " + str(Food.get_balance()))
print("Fun balance: " + str(Fun.get_balance()))
print("")

print("Withdraw 5 from food")
Food.withdraw(5, "test")
print("Food balance: " + str(Food.get_balance()))
print("Fun balance: " + str(Fun.get_balance()))
print("")

print("Transfer 6 from fun to food")
Fun.transfer(6, Food)
print("Food balance: " + str(Food.get_balance()))
print("Fun balance: " + str(Fun.get_balance()))
print("")

print("Check food funds with an amount of 11: ") 
print(Food.check_funds(11))
print("Check food funds with an amount of 14: ")
print(Food.check_funds(14))

print("")
print("")
print("Balance not ok")
print("**************")
print("")

print("Withdraw 14 from food")
Food.withdraw(14, "test")
print("Food balance: " + str(Food.get_balance()))
print("Fun balance: " + str(Fun.get_balance()))
print("")

print("Transfer 6 from fun to food")
Fun.transfer(6, Food)
print("Food balance: " + str(Food.get_balance()))
print("Fun balance: " + str(Fun.get_balance()))
print("")

#print(Food.get_balance())
#print(Fun.get_balance())


#print(Food.get_balance())