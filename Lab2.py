print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_bmi(height, weight): 
 print("Height = " + str(height)) 
 print("Weight = " + str(weight)) 
 print("BMI = " + str((weight/(height*height))))
 BMI = (weight/(height*height))
 if BMI < 18.5:
  print("Under Weight")
 elif BMI >= 18.5 and BMI <= 25.0:
  print("normal weight")
 elif BMI > 25.0:
  print("Over weight") 

  
calculate_bmi(weight=57, height=1.73)