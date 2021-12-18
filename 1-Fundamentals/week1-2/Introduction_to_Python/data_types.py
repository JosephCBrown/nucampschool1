"""
Declaing Variables
This is part of the 3. Variables and Data Types lesson
"""

x = 12.2
y = 7
z = 9.0

print(x)
print(y)
print(z)


print("THIS IS A BREAK TO THE NEXT SECTION OF LESSON..............")
"""
Primitve Data Types
"""
name = "Bob"  # Storing a String Value
age = 35  # Storing an Integer Value
cash = 100.25  # Storing a Float Value
retired = False  # Storing a Boolean Value

# How to Know the Data Type of a variable
# Invoking the function 'type(<VARIABLE NAME>)'
print("Data type of the variable 'name' is", type(name))
print("Data type of the variable 'age' is", type(age))
print("Data type of the variable 'cash' is", type(cash))
print("Data type of the variable 'retired' is", type(retired))


"""
Composite data types:
List, Dictionary, Tuple, Set
"""
print("THIS IS A BREAK TO THE NEXT SECTION OF LESSON..............")
nucamp_locations = ["Seattle", "Tacoma", "Bellevue"]  # Storing a List
Bob_Info = {"name": "Bob", "age": 35, "cash": 100.25,
            "retired": False}  # Storing a Dictionary
my_tuple = ("apple", "banana", "cherry")  # Storing a Tuple
my_set = {"cats", "dogs", "birds"}  # Storing a Set

print("Data type of the variable 'nucamp_locations' is", type(nucamp_locations))
print("Data type of the variable 'Bob' is", type(Bob_Info))
print("Data type of the variable 'my_tuple' is", type(my_tuple))
print("Data type of the variable 'my_set' is", type(my_set))
