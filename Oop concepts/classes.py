class account:
 def __init__(self,owner,bal):
    self.owner=owner
    self.bal=bal

 def deposit(self,amount):
       self.bal=self.bal + amount
       print(f"Sir {self.owner}   RS : {amount} is credited . Your new balance is {self.bal}")


 def withdraw(self,amount):
    if amount < self.bal:
      self.bal=self.bal - amount
      print(f"Sir {self.owner}   RS : {amount} is depited . Your new balance is {self.bal}")

    elif amount <= 0:
     print("Entered wrong amount ")

    else:
       print("Insufficient balanceL")



 def check_balance(self):
      print(f"Sir {self.owner} .Your balance is {self.bal}")

 def show_detail(self):
      print(f"Sir {self.owner} .Your balance is {self.bal}")


a1 = account("Saim" , 100000)
a1.deposit(500)
b = account("Haider" , 34000)
b.withdraw(5000)
print("====================================\n")
accounts=[]
accounts.append(a1)
accounts.append(b)

for x in accounts:
    x.show_detail()
