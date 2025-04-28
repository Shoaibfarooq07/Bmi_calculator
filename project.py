name=input("enter your name:")

weight=float(input("enter your weight in pounds:"))

height = float(input("enter your height in inches:"))

BMI = (weight * 703) / (height * height)

if BMI<18.5:
    print(f"{name} you are underweight")
elif BMI>=18.5 and BMI<=24.9:
    print(f"{name} you have normal weight")
elif BMI>=25 and BMI<=29.9:
    print(f"{name} you are overweight")
elif BMI>=30 and BMI<=34.9:
    print(f"{name} you are obese high")
elif BMI>=35 and BMI<=39.9:
    print(f"{name} you are Severely Obese	Very High")
elif BMI > 40:
    print(f"{name} you are 	Morbidly Obese	Extremely High")

else:
    print(f"{name} enter valid input")
    


# Under 18	Underweight	Minimal
# 18.5 - 24.9	Normal Weight	Minimal
# 25 - 29.9	Overweight	Increased
# 30 - 34.9	Obese	High
# 35 - 39.9	Severely Obese	Very High
# 40 and over	Morbidly Obese	Extremely High