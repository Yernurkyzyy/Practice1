# 1
class Vehicle:
    def move(self):
        print("Movement started")

class Bike(Vehicle):
    def ring(self):
        print("Bell: Ring-ring!")

my_bike = Bike()
my_bike.move()  # Inherited from Vehicle
my_bike.ring()  # Own method


# 2
class Employee:
    def work(self):
        print("Working...")

class Manager(Employee):
    def plan(self):
        print("Creating a plan...")


leader = Manager()
leader.work()  # Inherited from Employee
leader.plan()  # Own method


# 3
class Person:
    def eat(self):
        print("Eating...")

class Teacher(Person):
    def teach(self):
        print("Teaching a lesson...")

instructor = Teacher()
instructor.eat()   # Inherited from Person
instructor.teach() # Own method