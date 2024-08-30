weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in ft: "))

BMI = weight/ (height/100)**2

print("Your BMI is", BMI)

if BMI <=18.4:
    print("You are underweight")

elif BMI <= 25.5:
    print("You are healthy")

elif BMI <= 35.7:
    print("You are overwight")

elif BMI <= 40.6:
    print("You are obese")

else:
    print("You are severely obese.")