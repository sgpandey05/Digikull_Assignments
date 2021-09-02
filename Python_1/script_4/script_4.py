def bmi_script_4(height, weight):
     BMI = round(weight / (height * height), 1)
     print("The BMI is {}".format(BMI))
     return BMI

if __name__ == '__main__':
 
    age = int(input("Hi Argo, What is your Age? "))
    height = float(input("What is your Height in metres? "))
    weight = int(input("What is your Weight in Kg? "))
    output = bmi_script_4(height, weight)
    print(output)