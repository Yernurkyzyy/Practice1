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