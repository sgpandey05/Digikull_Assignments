import math
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def Circumference(self):
        return 2*math.pi*self.radius
    def __eq__(self, other):
             if self.radius==other.radius:
                return "Both Circle are Equal"
             elif self.radius < other.radius:
                 return "Circle 2 is bigger than Circle 1"
             else:
                  return "Circle 1 is bigger than Circle 2"

r1=int(input("Enter radius of circle: 1: "))
r2=int(input("Enter radius of circle: 2: "))
obj1=circle(r1)
obj2=circle(r2)
print("Area of circle:1 ",round(obj1.area(),2))
print("Area of circle:2 ",round(obj2.area(),2))
print("Circumference of circle:1 ",round(obj1.Circumference(),2))
print("Circumference of circle:2 ",round(obj2.Circumference(),2))
print(obj1==obj2)