
"""

@author: Daman Sen

Create a BMI (Body Mass index) calculator program that reads the user's weight
in kilograms and height in meters, then calculate and displays the user's body 
mass index.

"""

print("Welcome to the BMI calculator.\nTo get your BMI, fill in the following information.")
# enter height
# error in height
while True:
    try:
        height = float(input("Enter your height in meters:  "))
        if height > 0:
            break
        print(f"Invalid height entered, your entered height is {height}.")
    except Exception as e:
        print(e)       
# enter weight
# error in height
while True:
    try:
        weight = float(input("Enter your weight in kilograms:  "))
        if weight > 0:
            break
        print(f"Invalid hweight entered, your entered weight is {weight}.")
    except Exception as e:
        print(e)
print("\n")
# BMI formula
BMI = weight/(height**2)
#BMI values with three places after decimal.
if BMI < 18.5:
    print(f"Your BMI is {BMI:.3f}. You are under weight for your height.")
elif BMI >= 18.5 and BMI < 24.9:
    print(f"Your BMI is {BMI:.3f}. You are Normal for your height.")
elif BMI >= 25 and BMI < 29.9:
    print(f"Your BMI is {BMI:.3f}. You are Overweight for your height.")
elif BMI >= 30:
    print(f"Your BMI is {BMI:.3f}. You are Obese for your height.")
print("\n")
print("BMI Values")
print("%4s%20s" % ("Underweight:", "less then 18.5"))
print("%4s%32s" % ("Normal:", "Between 18.5 and 24.9"))
print("%4s%26s" % ("Overweight:", "Between 35 and 29.9"))
print("%4s%25s" % ("Obese:", "30 or greater"))
