"""
Part 1: Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area.

Expected Input/Output 1:

Enter length of rectangle: 2 
Enter breadth of rectangle: 2 
Area of rectangle: 4 
Expected Input/Output 2:

"""
import math
class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
    def area(self):
        return self.length*self.breadth

l=int(input("Enter length of rectangle : "))
b=int(input("Enter breadth of rectangle : "))
obj1=Rectangle(l,b)
print("Area of Rectangle : ",round(obj1.area(),2))
