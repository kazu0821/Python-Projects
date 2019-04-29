# Prompt the user to enter weight in pounds
weight = float(input("Enter weight in kilograms: "))
    
# Prompt the user to enter height in inches
height = float(input("Enter height in  Meters: "))
    
#KILOGRAMS_PER_POUND = 0.45359237 # Constant
#METERS_PER_INCH = 0.0254 # Constant 
    
# Compute BMI
weightInKilograms = weight  
heightInMeters = height 
bmi = weightInKilograms / (heightInMeters * heightInMeters)

# Display result
print("BMI is", bmi)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
