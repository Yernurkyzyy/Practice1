x = 7


print(x > 5 and x < 10) # True


print(x > 10 or x < 8)  # True


print(not(x > 5 and x < 10)) # False


y = ["apple", "cherry"]
print(len(y) > 1 and "apple" in y) # True


a = [1, 2]
b = [1, 2]
c = a
print(a is c)     # True
print(a is b)     # False 