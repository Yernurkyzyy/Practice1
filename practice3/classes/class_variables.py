# 1. Shared company name for all Employees
class Employee:
    company = "TechCorp"
    def __init__(self, name):
        self.name = name

# 2. Counter for total objects created
class Robot:
    count = 0
    def __init__(self):
        Robot.count += 1

# 3. Standard tax rate for a Store
class Store:
    tax_rate = 0.12
    def __init__(self, item_price):
        self.price = item_price

r1, r2, r3 = Robot(), Robot(), Robot()
print(f"Total robots: {Robot.count}") # 3