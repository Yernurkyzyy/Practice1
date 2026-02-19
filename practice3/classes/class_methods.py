# 1. Calculator class with instance methods
class Calculator:
    def add(self, a, b):
        return a + b
    def multiply(self, a, b):
        return a * b

# 2. Circle class with area method
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return 3.14 * (self.radius ** 2)

# 3. Light class with toggle method
class Light:
    def __init__(self):
        self.status = "OFF"
    def switch(self):
        self.status = "ON" if self.status == "OFF" else "OFF"
        print(f"Light is now {self.status}")

calc = Calculator()
print(calc.add(10, 5))