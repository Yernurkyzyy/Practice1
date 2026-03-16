fruits = ["apple", "banana", "cherry"]
prices = [100, 200, 300]

# enumerate(): Get index and value
print("Inventory List:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# zip(): Combine two lists into pairs
print("\nPrice Tags:")
for fruit, price in zip(fruits, prices):
    print(f"{fruit.capitalize()}: ${price}")