age = int(input("Enter your age: "))
message = ""
# if else statement
# if age >= 18:
#     message = "You are eligible for university"
# else:
#     message = "You are not eligible for university"
# ternary operator
message = "You are eligible for university" if age >= 18 else "You are not eligible for university"
print(message)


#
highIncome = input("Is your income high? (True/False): ")
goodCreditScore = input("Do you have a good credit score? (True/False): ")
educationStatus = input("Do you have a good education status? (True/False): ")
creditMessage = ""
educationMessage = ""

if highIncome.lower() == "true" and goodCreditScore.lower() == "true":
    creditMessage = "Eligible for loan"
else:
    creditMessage = "Not eligible for loan"
print(creditMessage + " creditMesssage from and")

# if one is true and the other isn't
if highIncome.lower() == "true" or goodCreditScore.lower() == "true":
    creditMessage = "Eligible for loan"
else:
    creditMessage = "Not eligible for loan"
print(creditMessage + " creditMesssage from or")

if not educationStatus.lower() == "true":
    educationMessage = "Eligible for loan"
else:
    educationMessage = "Not eligible for loan students aren't permitted to take on loans yet!"
print(educationMessage + " educationMessage from not")


# all used at once
if highIncome.lower() == "true" and goodCreditScore.lower() == "true" and age >= 18 and (not educationStatus.lower() == "true"):
    print("Business is booming in this time of the year let's get to work!")
else:
    print("Improve on your income, credit score, age, and education status to be eligible for a loan! and you're a student step up")


# age should be between 18 and 65
if age >= 18 and age <= 65:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

if 18 <= age < 65:
    print("Eligible for loan")
else:
    print("Not eligible for loan") 

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")