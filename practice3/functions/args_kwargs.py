#1
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Lia", "Rano", "Alina")


#2
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emilia", "Nati", "Tiko")


#3
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")