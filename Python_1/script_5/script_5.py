def bmi_script_4(height, weight):
    BMI = round(weight / (height * height), 1)
    return BMI


def compare(BMI):

    if BMI < 18.5:
        print("Your BMI is {} which means you are underweight".format(BMI))
    elif BMI > 18.5 and BMI < 24.9:
        print("Your BMI is {} which means you are healthy".format(BMI))
    elif BMI > 25.0 and BMI < 29.9:
        print("Your BMI is {} which means you are overweight".format(BMI))
    elif BMI > 30.0:
        print("Your BMI is {} which means you are obese".format(BMI))
    else:
        print("Enter Valid Details")

if __name__ == '__main__':
    
    name = input("What is your Name: ")
    age = int(input("Hi {}, What is your Age? ".format(name)))
    height = float(input("What is your Height in metres? "))
    weight = int(input("What is your Weight in Kg? "))
    compare(bmi_script_4(height, weight))






# BMI = bmi_script_4(height, weight)  # y??
     