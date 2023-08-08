#print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")


class Category:

  def __init__(self, name):
    #When initialised, the name of the category is input
    self.name = name
    self.ledger = []
    self.balance = 0

  def __str__(self):

    #Header for the output, with the category in the center:
    heading_half_length = int((30 - len(self.name)) / 2)
    heading_half_str = ''
    for n in range(heading_half_length):
      heading_half_str += '*'
    heading_str = "{}{}{}\n".format(heading_half_str, self.name,
                                    heading_half_str)

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

      #Appends the truncated amounts to the empty list:
      for n in range(amount_length):
        amount += str(item['amount'])[n]
      amounts_list.append(amount)

    #Initialise the empty string to be output, and add the heading:
    string_out = ''
    string_out += heading_str

    for n in range(len(self.ledger)):

      string_out += description_list[n] + amounts_list[n] + '\n'
    string_out += 'Total: {}'.format(round(float(self.balance), 2))

    return string_out
    #return "*************{}*************\n".format(self.name)

  #Method to deposit to a category, with the amound and description being added to the ledger:
  def deposit(self, amount, description=''):
    self.deposit_info = {'amount': amount, 'description': description}
    self.ledger.append(self.deposit_info)
    self.balance += amount
    print(self.balance)

  #Method to withdraw from the ledger
  def withdraw(self, amount, description=''):
    #Use the check_funds method to ensure this only occurs when there is enough funds:
    if self.check_funds(amount):
      self.withdraw_info = {'amount': -amount, 'description': description}
      self.ledger.append(self.withdraw_info)
      self.balance -= amount
      print(self.balance)
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

  #def create_spend_chart(categories):
  #  pass


def create_spend_chart(categories):
  number_of_categories = len(categories)
  print(number_of_categories)
  #Empty dictionaries to store the category information:
  category_dict = {}
  #print(category_dict)
  category_percent = []
  percent_list = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
  category_chart_percents = []
  category_chart_names = []

  #Empty variable to store the total spent, to calculate the percentages:
  total_spent = 0
  #print(category_percent)

  #Loop to add the amounts spent in each category to category_dict:
  for category in categories:
    #Initialise the dicts with zero values:
    category_dict[category.name] = 0
    #category_percent[category.name] = 0

    #Loop through ledger in each category to find the withdrawals:
    for item in category.ledger:
      #print(item)

      #Test if a withdrawal, then add the positive value to the dict if so:
      if item["amount"] < 0:
        #print("withdrawal")
        #print(item["amount"])
        category_dict[category.name] += item["amount"] * -1
        #print(category_dict)
        #print(category.balance)

  #Loop through the categories to get the total spent and calculate the percentages to be used in the chart:
  for category in categories:
    total_spent += (category_dict[category.name])
  for category in categories:
    category_percent.append((category_dict[category.name] / total_spent) * 100)
    #category_percent[category.name] += (category_dict[category.name]/category.balance) * 100
  #print(total_spent)
  #print(category_dict)
  print(category_percent)

  #Add percents to list:
  for n in range(len(percent_list)):
    category_chart_percents.append("")
    category_chart_percents[n] += str(percent_list[n]) + '|'

  print(category_chart_percents)

  #Loop through categories and add the ' o  ' if required:
  for n in range(len(percent_list)):
    print(n)
    for m in range(number_of_categories):
      if category_percent[m] > percent_list[n]:
        category_chart_percents[n] += ' o '
      else:
        category_chart_percents[n] += '   '

  print(category_chart_percents)
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

print("Deposit 100 into Food")
Food.deposit(100, "Initial Food deposit")
print("")

print("Deposit 200 into Fun")
Fun.deposit(200, "Initial Fun deposit")
print("")

print("Withdraw 5.99 from food")
Food.withdraw(5.99, "Meal")
print("")

print("Withdraw 50.65 from food")
Food.withdraw(50.65, "Food shop")
print("")

print("Withdraw 40.50 from fun")
Fun.withdraw(40.50, "Concert ticket")
print("")

print("Transfer 6.28 from fun to food")
Fun.transfer(6.28, Food)
print("")

print(Food)
print("")

print(Fun)
print("")

create_spend_chart([Food, Fun])

#print(Food.get_balance())
#print(Fun.get_balance())

#print(Food.get_balance())
