#1
class Parent:
    def __init__(self, last_name):
        self.last_name = last_name

class Child(Parent):
    def __init__(self, first_name, last_name):
       
        super().__init__(last_name)
        self.first_name = first_name

    def full_name(self):
        print(f"{self.first_name} {self.last_name}")

c = Child("Sara", "Smith")
c.full_name()

class Device:
    def power_on(self):
        print("Device is booting up...")

class Laptop(Device):
    def power_on(self):
   
        super().power_on()
       
        print("Laptop: Loading Windows/macOS desktop.")


my_laptop = Laptop()
my_laptop.power_on()


# 3
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"Product: {self.name}, Price: ${self.price}"

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period

    def get_details(self):
        
        basic_info = super().get_details()
        return f"{basic_info}, Warranty: {self.warranty_period} months"


phone = ElectronicProduct("iPhone 15", 999, 12)
print(phone.get_details())