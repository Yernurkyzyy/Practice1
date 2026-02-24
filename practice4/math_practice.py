import math
import random

# 1
numbers = [10, 25, 5, 40]
print("Max value:", max(numbers))     # 40
print("Absolute value:", abs(-7.5))   # 7.5
print("Power (2^3):", pow(2, 3))      # 8

# 2
print("Square root of 16:", math.sqrt(16))      # 4.0
print("Ceil (round up) 4.2:", math.ceil(4.2))    # 5
print("Floor (round down) 4.8:", math.floor(4.8)) # 4
print("Pi value:", math.pi)                      # 3.1415...

# 3
random_num = random.randint(1, 100)
print("Random number (1-100):", random_num)

# Random choice from a list
fruits = ["Apple", "Banana", "Cherry"]
print("Random fruit:", random.choice(fruits))

# Shuffling a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)