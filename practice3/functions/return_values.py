# 1. Returning a simple calculation
def calculate_tax(price):
    return price * 0.12

# 2. Returning a boolean (True/False)
def is_adult(age):
    return age >= 18

# 3. Returning multiple values as a tuple
def get_min_max(numbers):
    return min(numbers), max(numbers)

# Examples
print(calculate_tax(1000))
print(is_adult(20))
print(get_min_max([1, 5, 10]))