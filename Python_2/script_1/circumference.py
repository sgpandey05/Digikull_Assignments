# Write a script to get circumference of a circle. 
# Import math module to get value of pi. 
# Take radius of circle as input from User
import math
radius = float(input("Enter Radius of Circle :"))
p = math.pi
circumference = (2*p*radius)
print("circumference of circle is {} ".format(circumference))