#Name:Raphael Hennings
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

print("This BMI calculator is fro people 19=<")
Height = int(input("Enter your height in centimeters: "))
Weight = int(input("Enter your weight in kilograms: "))

print(Height)
print(Weight)

BMI = Weight/((Height/100)**2)

print(BMI)

if BMI < 18.5:
    print("You are underweight")
elif 24.9 > BMI > 18.5:
    print("You are normal")
elif 29.5 > BMI > 25:
    print("You are overweight")
else:
    print("You are obese")


#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification