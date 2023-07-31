class Category:
    #Class variables that will be referenced:
    ledger = []
    balance = 0
    
    def __init__(self, name):
        #When initialised, the name of the category is input
        self.name = name
    
    def __str__(self):
        string_out = "*************{}*************\n".format(self.name) 
        #for item in self.ledger:
        #    string_out += item[1]
        for item in self.ledger:
            description = str(item['description'])
            amount = str(item['amount'])
            string_out += description + ': ' + amount + '\n'
        string_out += '\nTotal: {}'.format(self.balance)
        
        return string_out
        #return "*************{}*************\n".format(self.name)
        
    
    #Method to deposit to a category, with the amound and description being added to the ledger:
    def deposit(self, amount, description = ''):
        self.deposit_info = {'amount': amount, 'description': description}
        self.ledger.append(self.deposit_info)
        self.balance += amount
    
    #Method to withdraw from the ledger
    def withdraw(self, amount, description = ''):
        #Use the check_funds method to ensure this only occurs when there is enough funds:
        if self.check_funds(amount):
            self.withdraw_info = {'amount': -amount, 'description': description}
            self.ledger.append(self.withdraw_info)            
            self.balance -= amount
            return True
        else:
            return False
    
    #Method to return the balance of the category:
    def get_balance(self):
        return self.balance
    
    #Method to transfer between categories
    def transfer(self, amount, category):
        #Logic to ensure enough funds exist to transfer, and return the appropriate result:
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to {}".format(category.name))
            category.deposit(amount, "Transfer from {}".format(self.name))
            return True
        else:
            return False
            
    #Method used to check if enough funds exist for a specified amount:
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

#print("Check food funds with an amount of 11: ") 
#print(Food.check_funds(11))
#print("Check food funds with an amount of 14: ")
#print(Food.check_funds(14))

#print("")
#print("")
#print("Balance not ok")
#print("**************")
#print("")

#print("Withdraw 14 from food")
#Food.withdraw(14, "test")
#print("Food balance: " + str(Food.get_balance()))
#print("Fun balance: " + str(Fun.get_balance()))
#print("")

#print("Transfer 6 from fun to food")
#Fun.transfer(6, Food)
#print("Food balance: " + str(Food.get_balance()))
#print("Fun balance: " + str(Fun.get_balance()))
#print("")

print(Food)
print("")

#print(Food.get_balance())
#print(Fun.get_balance())


#print(Food.get_balance())