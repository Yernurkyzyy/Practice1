from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map(): Square each number
squares = list(map(lambda x: x**2, numbers))
print(f"Squares: {squares}")

# filter(): Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# reduce(): Calculate sum of all elements
total_sum = reduce(lambda x, y: x + y, numbers)
print(f"Total Sum: {total_sum}")