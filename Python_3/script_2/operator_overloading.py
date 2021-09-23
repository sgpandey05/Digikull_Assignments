'''
Part 1: Define a class named Circle which can be constructed by a radius.
Compare two circles objects and return True if circles are equal. 
Return False if circles are not equal Take radius of these circles through Input

Expected Input/Output 1:

Enter Radius of Circle 1: 2 Enter Radius of circle 2: 4 Output: False 

Expected Input/Output 2:

Enter Radius of Circle 1: 8 Enter Radius of circle 2: 8 Output: True
'''

# import math
# class circle():
#     def __init__(self,radius):
#         self.radius=radius

# r1=int(input("Enter radius of circle: 1: "))
# r2=int(input("Enter radius of circle: 2: "))
# obj1=circle(r1)
# obj2=circle(r2)
# print(r1==r2)

class circle:
      def __init__(self, radius):
            self.comp=radius
           

      def __eq__(self, other):
             if self.comp==other.comp:
                  return "True"
             else:
                  return "False"

r1 = int(input("Enter Radius of Circle 1 : "))
r2 = int(input("Enter Radius of Circle 2 : "))
obj1=circle(r1)
obj2=circle(r2)
print (obj1==obj2)
