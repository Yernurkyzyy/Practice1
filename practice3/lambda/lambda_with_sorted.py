# 1. Sorting a list of strings by their length
names = ["Alexander", "Ali", "Zeynep", "Bo"]
sorted_names = sorted(names, key=lambda x: len(x))
print(f"Sorted by length: {sorted_names}")

# 2. Sorting a list of tuples by the second element (price)
products = [("Apple", 50), ("Banana", 20), ("Cherry", 80)]
sorted_products = sorted(products, key=lambda item: item[1])
print(f"Sorted by price: {sorted_products}")

# 3. Sorting a list of dictionaries by a specific key
students = [{"name": "John", "score": 88}, {"name": "Jane", "score": 95}, {"name": "Doe", "score": 82}]
top_students = sorted(students, key=lambda s: s['score'], reverse=True)
print(f"Top students: {top_students}")