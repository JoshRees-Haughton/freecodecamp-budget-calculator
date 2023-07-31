class Category:
    #Class variables that will be referenced:
    ledger = []
    balance = 0
    
    def __init__(self, name):
        #When initialised, the name of the category is input
        self.name = name
    
    def __str__(self):
        
        heading_half_length = int((30 - len(self.name))/2)
        heading_half_str = ''
        for n in range(heading_half_length):
            heading_half_str += '*'
        heading_str = "{}{}{}\n".format(heading_half_str, self.name, heading_half_str)
        #print(heading_str)
        
        #Header for the output, with the category in the center:
        #string_out = "*************{}*************\n".format(self.name)
        
        #Empty lists to stor the description and amount strings:
        description_list = []
        amounts_list = []
        
        #Loop through the items in the eldger:
        for item in self.ledger:
            description = ''
            amount = ''
            #Calculates the description output lengths, with the maximum description being 23 characters:
            if len(item['description']) <= 23:
                description_length = len(item['description'])
            else:
                description_length = 23
                
            #Calculate the amount length, with a maximum length of 7:
            if len(str(item['amount'])) <= 7:
                amount_length = len(str(item['amount']))
            else:
                amount_length = 7
                
            #The length of the space after the description:
            space_length = 30 - description_length - amount_length
            
            
            #Adds the characters to the descriptions:
            for n in range(description_length):
                description += item['description'][n]
            #Adds the space characters:
            for m in range(space_length):
                description += ' '
            #Adds the descriptions to the list to be used later:
            description_list.append(description)
        #print(description_list)
            
            for n in range(amount_length):
                amount += str(item['amount'])[n]
            amounts_list.append(amount)
            
        
        string_out = ''
        string_out += heading_str
                

        for n in range(len(self.ledger)):

            
            string_out += description_list[n] + amounts_list[n] + '\n'
        string_out += 'Total: {}'.format(round(float(self.balance), 2))
        
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

print("Deposit 12.34 into Food")
Food.deposit(12.34, "1234567891011121314151617181920")
print("Food balance: " + str(Food.get_balance()))
print("Fun balance: " + str(Fun.get_balance()))
print("")

print("Deposit 11.12 into Fun")
Fun.deposit(11.12, "test")
print("Food balance: " + str(Food.get_balance()))
print("Fun balance: " + str(Fun.get_balance()))
print("")

print("Withdraw 5 from food")
Food.withdraw(5.99, "test")
print("Food balance: " + str(Food.get_balance()))
print("Fun balance: " + str(Fun.get_balance()))
print("")

print("Transfer 6 from fun to food")
Fun.transfer(6.28, Food)
print("Food balance: " + str(Food.get_balance()))
print("Fun balance: " + str(Fun.get_balance()))
print("")


print(Food)
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



#print(Food.get_balance())
#print(Fun.get_balance())


#print(Food.get_balance())