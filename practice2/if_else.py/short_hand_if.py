a = 200
b = 33

#1
if a > b: print("a is greater than b")

#2
print("A") if a > b else print("B")

#3
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#4
status = "Allow" if age >= 18 else "Block"
print(status)

#5
if a > b and b > 0: print("Both conditions are True")