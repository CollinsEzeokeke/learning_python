course = "Python Programming"
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