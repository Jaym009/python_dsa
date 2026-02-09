# CREATE
# READ
# UPDATE
# DELETE

# Comments in Python
# Single Line Comment
# This is a Single Line Comment
# Multi Line Comment
"""
This is a Multi Line Comment
Here I can keep on adding comments
python is a case-sensitive language
thisVariable and thisvariable are two different variables
Indentation is very important in Python, it defines the block of code, similar to curly braces {} in other programming languages

Line Continuation
You can use a backslash (\) to continue a line of code onto the next line
total = 1 + 2 + 3 + \
        4 + 5 + 6

Alternatively, you can use parentheses to span multiple lines
total = (1 + 2 + 3 +
            4 + 5 + 6)

print(total)

Multiple Statements on a Single Line
You can write multiple statements on a single line using a semicolon (;)
x = 5; y = 10; print(x + y)
"""


# Declaring a Variable
# CREATING a Variable
name="John Doe"
age=30
# READING a Variable
print(name)
print(age)
# UPDATING a Variable
age=31
print(age)
# DELETING a Variable
del name
# print(name) # This will raise an error as name variable is deleted

# Data Types in Python
# String
name = "John Doe"  # String
# Integer
age = 30           # Integer
# Float
height = 5.9       # Float
# Boolean
is_student = False # Boolean

# To Read the Type of a variable in Python, we use the type() method
print(type(age))  # Output: <class 'int'>

# Operators in Python
# Conditional Statements
if age > 18:
    print("Adult")
# Control Flow Statements
# Loops
# Declaring a Function
# Declaring a Class, Method, Properties and an Object
# Access Modifiers
# In Built Classes
# In Built Methods