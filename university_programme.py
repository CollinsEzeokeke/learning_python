age = int(input("Enter your age: "))
message = ""
if age >= 18:
    message = "You are eligible for university"
else:
    message = "You are not eligible for university"

message = "You are eligible for university" if age >= 18 else "You are not eligible for university"
print(message)