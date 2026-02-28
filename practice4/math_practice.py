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


#1Write a Python program to convert degree to radian. Input degree: 15 Output radian: 0.261904
import math

degree = 15
# radian = degree * (pi / 180)
radian = math.radians(degree)

print(f"Input degree: {degree}")
print(f"Output radian: {radian:.6f}")


#2 Write a Python program to calculate the area of a trapezoid. Height: 5. Base, first value: 5. Base, second value: 6. Expected Output: 27.5
height = 5
base1 = 5
base2 = 6

# Area = ((a + b) / 2) * h
area = ((base1 + base2) / 2) * height

print(f"Height: {height}")
print(f"Base, first value: {base1}")
print(f"Base, second value: {base2}")
print(f"Expected Output: {area}")

#3 Write a Python program to calculate the area of regular polygon. Input number of sides: 4. Input the length of a side: 25. The area of the polygon is: 625
import math

n_sides = 4
side_length = 25

# Area = (n * s^2) / (4 * tan(pi / n))
area = (n_sides * side_length**2) / (4 * math.tan(math.pi / n_sides))

print(f"Input number of sides: {n_sides}")
print(f"Input the length of a side: {side_length}")
print(f"The area of the polygon is: {area:.0f}")


#4 Write a Python program to calculate the area of a parallelogram. Length of base: 5. Height of parallelogram: 6. Expected Output: 30.0
base_length = 5
height_para = 6

# Area = base * height
area_para = float(base_length * height_para)

print(f"Length of base: {base_length}")
print(f"Height of parallelogram: {height_para}")
print(f"Expected Output: {area_para}")