import math

# 1
def iterator_demo():
    print("--- 1. Iterator Demo ---")
    fruits = ["apple", "banana", "cherry"]
    my_it = iter(fruits)
    
    print(next(my_it))  # apple
    print(next(my_it))  # banana
    print(next(my_it))  # cherry
    print()

#2. 
def square_generator(n):
    """Generates squares of numbers from 1 up to n"""
    for i in range(1, n + 1):
        yield i ** 2

# 3
def even_generator(n):
    """Generates only even numbers up to n"""
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

#4
def gen_expression_demo(n):
    print("--- 2. Generator Expression Demo ---")
    squares_exp = (x**2 for x in range(n))
    
    for val in squares_exp:
        print(val, end=" ")
    print("\n")


if __name__ == "__main__":
    
    iterator_demo()

  
    try:
        user_num = int(input("Enter a number for generation: "))
        
        
        print(f"\nSquares up to {user_num}:")
        for num in square_generator(user_num):
            print(num, end=" ")
        
        
        print(f"\n\nEven numbers up to {user_num}:")
        evens = even_generator(user_num)
        
        print("First even:", next(evens))
        print("Second even:", next(evens))
        
        print("\nAll remaining even numbers:")
        for e in evens:
            print(e, end=" ")
        print("\n")

        
        gen_expression_demo(5)

    except ValueError:
        print("Error: Please enter a valid integer.")


#1 Create a generator that generates the squares of numbers up to some number N.
def squares_generator(n):
    for i in range(1, n + 1):
        yield i ** 2

n = 5
for val in squares_generator(n):
    print(val, end=" ")

#2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield str(i)


n = int(input("Enter n: "))
evens = even_generator(n)

print(", ".join(evens))


#3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for num in divisible_by_3_4(50):
    print(num, end=" ")


#4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares_range(a, b):
    for i in range(a, b + 1):
        yield i ** 2


a, b = 3, 6
print(f"Squares from {a} to {b}:")
for val in squares_range(a, b):
    print(val) 


#5 Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for x in countdown(5):
    print(x, end=" ")