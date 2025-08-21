# Create a class Vehicle with attributes brand and year. Derive a class Car that adds model, and override a method display() to print full details.

class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def display(self):
        print("I am printing from vehicle class")

class Car(Vehicle):

    def __init__(self,brand,year,model):
        super().__init__(brand,year)
        self.model=model

    def display(self):
        print(f"the model of car is {self.brand} and year {self.year} and model {self.model}")

vehicle1=Vehicle("bmw",2025)
vehicle1.display()

car1=Car("audi",2025,"a6")
# car1.display()
        
# Create a class Employee with attributes name and salary. Derive a class Manager that adds department. Use super() to initialize base attributes.

class Employee:
    name=None
    salary=None

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept

    def detail(self):
        print(self.name,self.salary,self.dept)

mng=Manager("Shekher",10,"automation")
mng.detail()


# Create a polymorphic function that takes a list of different Shape objects (Circle, Rectangle, Triangle) and prints their area.
import math
class Shape:
    def __init__(self,var):
        self.var=var

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
class Rectangle(Shape):
    def __init__(self, l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
class Triangle(Shape):
    def __init__(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        return (1/2)*(self.b*self.c)
    
c1=Circle(5)
r1=Rectangle(5,4)
t1=Triangle(2,4,6)

print(c1.area(),"and ",r1.area(),t1.area())
    