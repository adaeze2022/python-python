height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

#BMI = the weight divided by the square of the height
height_value = float(height)
weight_value = int(weight)

BMI = round(weight_value / height_value ** 2)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight!")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight!")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are overweight!")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese!")
else:
    print(f"Your BMI is {BMI}, youa re clinically obese; please seek medical help!")
