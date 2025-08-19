# Create a class Car with attributes: brand, model, and year. Add a method to display details.

class Car:
     def __init__(self,brand,model,year):
          self.brand=brand
          self.model=model
          self.year=year
     
     def display(self):
          print("The brand is",self.brand) 
          print(f"The model is {self.model}")
          print(f"The year of manufacture is {self.year}")


car1=Car("bmw","m5","2025")
# car1.display()


# Create a class BankAccount with methods: deposit, withdraw, and check_balance.

class BankAccount:
     def __init__(self,acct,bal):
          self.acct=acct
          self.bal=bal

     def deposit(self,amount):
          self.bal+=amount
          print(f"{amount} deposit successfully")

     def withdraw(self,amount):
          if(self.bal<amount):
               print("Account doesn't have sufficient amount")
          else:
               self.bal-=amount

     def checkbalance(self):
          print(self.bal)


account1=BankAccount(1011212,10000)
# account1.checkbalance()
# account1.deposit(2000)
# account1.checkbalance()
# account1.withdraw(10000000)
# account1.withdraw(100)
# account1.checkbalance()


# Write a class Rectangle with methods to calculate area and perimeter.

class Rectangle:
     def __init__(self,len,width):
          self.len=len
          self.width=width
     def area(self):
          print(self.len*self.width)

     def perimeter(self):
          print(2*(self.len+self.width))

rect1=Rectangle(10,20)

# rect1.area()
# rect1.perimeter()


# Create a class Employee with a class variable company = "Google" and instance variables name, salary. Print details for 2 employees.

class Employee:
     company="Google"

     def __init__(self,name,salary):
          self.name=name
          self.salary=salary

     def details(self):
          print(self.name,self.salary,self.company)


emp1=Employee("Kushagra",5000000)
emp2=Employee("Abhishek",120000)

# emp1.details()
# emp2.details()
            

# Create a Calculator class with add, subtract, multiply, divide as static methods.

class Calculator:
     
     def __init__(self):
          pass

     @staticmethod
     def  add(a,b):
          print(a+b)

     @staticmethod
     def sub(a,b):
          print(a-b)
     @staticmethod
     def mul(a,b):
          print(a*b)
     @staticmethod
     def div(a,b):
          print(a/b)

calc1= Calculator()
calc1.add(10,20)
calc1.sub(20,10)
calc1.mul(2,3)
calc1.div(20,5)
          
          
     
     

