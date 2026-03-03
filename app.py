import math

course = "   Python Programming"
numberDefined = 12
# tripple quotes stings
message = """
Hi John,

This is a multi-line string.
"""
# len function for getting length of a string
lenghtNumber = len(course)
print(lenghtNumber)
# indexing
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

# escape sequences
# \"
# \n
# \t
# \r
# \b
# \f
# \v
# \\

newCourse = "Python \nProgramming "
print(newCourse)

first = "John"
last = "Doe"
full_name = first + " " + last
print(full_name)

# formatted strings
print(f"Hello there {first} {last} {numberDefined}")

strippedCourse = course.strip()
print(strippedCourse)

# string methods
print(course.upper())
print(course.lower())
print(course.title())
print(strippedCourse)
print(course)
parsedVar = course.lower()
print(parsedVar.find("pro"))
print(course.replace("Python", "Java"))
print("pro" in course)
print("Pro" in course)
print("pro" not in course)


# numbers
x = 1
y = 1.1
x = 1 + 2j  # a + bi complex numbers
print(x + y)

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)


# augumented
x = 10
print(x)
# x = x + 3  #same as below
x += 3
print(x)


# number functions
print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2))


# input functions
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y} and y has a type of {type(y)} while x has a type of {type(x)}")


# checking types
# print(type(x))

# various conversions in python
# print(int(x))
# print(float(x))
# print(str(x))
# print(bool(x))
# print(list(x))
# print(tuple(x))
# print(set(x))
# print(dict(x))
# print(type(x))

# Boolean falsy contexts
# ""
# 0
# None
# []
# {}
# ()

# Boolean truthy contexts
# "Hello"
# 1
# None
# [1]
# {1}
# (1)

fruit = "Apple"
print(fruit[1:-1])


# comparison operators
print(1 == 1)
print(1 != 1)
print(1 > 0)
print(1 < 10)
print(10 >= 1)
print(1 <= 10)

# comparison operators on strings
print("bag" > "apple")  # True
print("bag" == "BAG")  # False
comparison_b = ord("b")
# number calculations of teh stings
print(f"{ord("b")} , {ord("a")} , {ord("g")}")
print(f"{ord("B")} , {ord("A")} , {ord("G")}")
capitals = ord("B") + ord("A") + ord("G")
print(capitals)
print(chr(capitals))  # converts the number to a character
littles = ord("b") + ord("a") + ord("g")
print(littles)
print(chr(littles))
print(
    f"The difference between capitals and littles is {capitals - littles}, is capitals greater: {capitals > littles}, what's the type? {type(capitals)}, {type(littles)}")

# conditional statements
temperature = int(input("what's the temperature like today? "))
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
    print("Enjoy the day")
else:
    print("It's cold")
    print("Wear a jacket")
print("Done!!")
