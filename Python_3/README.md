# python_third_assignment

Script 1: Decorators:
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate

Functions in Python are first-class citizens. This means that they support operations such as being passed as an argument, returned from a function, modified, and assigned to a variable. This is a fundamental concept to understand before we delve into creating Python decorators.

Before you can understand decorators, you must first understand how functions work. For our purposes, a function returns a value based on the given arguments. Here is a very simple example:
Example 1:


def add_one(number):
return number + 1

add_one(2)
3
To understand decorators, it is enough to think about functions as something that turns given arguments into a value.

Consider this example, This decorator swaps the value of a and b if a<b. So if the user pass the parameter as (2,4) or (4,2). The output of division is always bigger_number/smaller_number i.e 4/2


Example:
def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
	if a<b:
	    a,b = b,a
	return func(a,b)

    return inner
    
div = smart_div(div)

div(4,2)
#Output:  2.0

div(2,4)
#Output:  2.0

We will generate a decorator that will simply capitalize the string output of a function

The capitalize_names function acts as a decorator that takes a function as an argument. The inner func_wrapper function has access to the function argument via closures and modifies the function. The capitalize_name decorator then returns the result of the func_wrapper function.

The most important part of the code snippet however is the assignment expression
get_fullname = capitalize_names(get_fullname)<br />
This ensures that the original function get_fullname becomes replaced by the modified (decorated) function returned by the capitalize_names decorator.


def get_fullname(firstname, lastname):
    return "{}, {}".format(lastname, firstname)

def capitalize_names(func):
    def func_wrapper(fname, lname):
	return func(fname, lname).upper()
    return func_wrapper

get_fullname = capitalize_names(get_fullname)
print(get_fullname(Tom, Holland))

#Output: HOLLAND, TOM

Part 1 :
Create a decorator to print a statement n no. of times.
n is the number of times you want to print a statement

Example INPUT/OUTPUT 1

What do you want to print?
>> Hello World
How many times do you want to print the statement?
>> 5
#OUTPUT
Hello World
Hello World
Hello World
Hello World
Hello World
Example INPUT/OUTPUT 2

What do you want to print?
>> Stranger Things
How many times do you want to print the statement?
>> 0
#OUTPUT
Example INPUT/OUTPUT 3

What do you want to print?
>> Stranger Things
How many times do you want to print the statement?
>> -1
#OUTPUT
Please provide a positive number
Example INPUT/OUTPUT 4

What do you want to print?
>> Stranger Things
How many times do you want to print the statement?
>> 3
# OUTPUT
Stranger Things
Stranger Things
Stranger Things

Write the code in script_1/decorator_1.py

Python’s decorator syntactic sugar (Refer Example 2 above)
Python provides a syntactic sugar to make the creation and usage of a decorator cleaner and nicer. The general assignment expression syntax of a decorator;
get_fullname = capitalize_names(get_fullname)
can be replaced with a shortcut. The name of decoration function prepended with an @ symbol is mentioned before the definition of the function to be decorated

@capitalize_names<br />
def get_fullname(firstname, lastname):
    return "{}, {}".format(lastname, firstname)

This behaviour is the syntactic sugar because writing @decorator above the function definition is the same as calling f = decorator(f) after it.


Script 2: Operator Overloading

Python operators work for built-in classes. But the same operator behaves differently with different types. For example, the + operator will perform arithmetic addition on two numbers, merge two lists, or concatenate two strings.

This feature in Python that allows the same operator to have different meaning according to the context is called operator overloading.
Overloading the + Operator
To overload the + operator, we will need to implement add() function in the class. With great power comes great responsibility. We can do whatever we like, inside this function. But it is more sensible to return a Point object of the coordinate sum.

class Point:
    def __init__(self, x=0, y=0):
	self.x = x
	self.y = y

    def __str__(self):
	return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
	x = self.x + other.x
	y = self.y + other.y
	return Point(x, y)

p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2)

#Output
(3,5)
Overloading the comparison Operator

#Python program to overload
#a comparison operators
class A: 
    def __init__(self, a): 
	self.a = a 
    def __gt__(self, other): 
	if(self.a>other.a): 
	    return True
	else: 
	    return False
ob1 = A(2) 
ob2 = A(3) 
if(ob1>ob2): 
    print("ob1 is greater than ob2") 
else: 
    print("ob2 is greater than ob1")

Output :
ob2 is greater than ob1
Part 1:
Define a class named Circle which can be constructed by a radius. Compare two circles objects and return True if circles are equal. Return False if circles are not equal
Take radius of these circles through Input


Expected Input/Output 1:

Enter Radius of Circle 1: 2
Enter Radius of circle 2: 4
Output: False
Expected Input/Output 2:

Enter Radius of Circle 1: 8
Enter Radius of circle 2: 8
Output: True
Write the code in script_2/operator_overloading.py

Script 3: Object-oriented programming (OOP)
Object-oriented programming (OOP) is based on the concept of “objects,” which can contain data and code: data in the form of instance variables (often known as attributes or properties), and code, in the form method. I.e., Using OOP, we encapsulate related properties and behaviors into individual objects. Knowledge of OOP is necessary if you want to be a good Python developer

Some common words related to OOPS:

• class—Tell Python to make a new kind of thing.
• object—Two meanings: the most basic kind of thing, and any instance of some thing.
• instance—What you get when you tell Python to create a class.
• def—How you define a function inside a class.
• self—Inside the functions in a class, self is a variable for the instance/object being accessed.
• inheritance—The concept that one class can inherit traits from another class, much like you and your parents.
• composition—The concept that a class can be composed of other classes as parts, much like how a car has wheels.
• attribute—A property classes have that are from composition and are usually variables.
• is-a—A phrase to say that something inherits from another, as in a “salmon” is-a “fish.”
• has-a—A phrase to say that something is composed of other things or has a trait, as in “a salmon has-a mouth.”


class X(Y) “Make a class named X that is-a Y.”
class X(object): def init(self, J) “class X has-a init that takes self and J parameters.”
class X(object): def M(self, J) “class X has-a function named M that takes self and J parameters.”
foo = X() “Set foo to an instance of class X.”
foo.M(J) “From foo get the M function, and call it with parameters self, J.”
foo.K = Q “From foo get the K attribute, and set it to Q.”

Example 1: Classes and Objects

class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
	self.name = name
	self.age = age

#instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

#access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

#access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

#Output
Blu is a bird
Woo is also a bird
Blu is 10 years old
Woo is 15 years old
In the above program, we created a class with the name Parrot. Then, we define attributes. The attributes are characteristic of an object.

These attributes are defined inside the init method of the class. It is the initializer method that is first run as soon as the object is created.

Then, we create instances of the Parrot class. Here, blu and woo are references (value) to our new objects.

We can access the class attribute using class.species. Class attributes are the same for all instances of a class. Similarly, we access the instance attributes using blu.name and blu.age. However, instance attributes are different for every instance of a class.


Example 2: Methods

class Parrot:

    # instance attributes
    def __init__(self, name, age):
	self.name = name
	self.age = age

    # instance method
    def sing(self, song):
	return "{} sings {}".format(self.name, song)

    def dance(self):
	return "{} is now dancing".format(self.name)

#instantiate the object
blu = Parrot("Blu", 10)

#call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
Output
Blu sings 'Happy'
Blu is now dancing
Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.

In the above program, we define two methods i.e sing() and dance(). These are called instance methods because they are called on an instance object i.e blu.

Part 1:
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

Expected Input/Output 1:

Enter length of rectangle: 2
Enter breadth of rectangle: 2
Area of rectangle: 4
Expected Input/Output 2:

Enter length of rectangle: 1
Enter breadth of rectangle: 1
Area of rectangle: 1
Write the code in script_3/rectangle.py

Part 2:
Define a class named Circle which can be constructed by a radius. The Circle class has 4 methods which can

compute the circumference and
area of both circle
able to add two circles
Compare two circles and find which is bigger
Check if the circles are equal

Expected Input/Output 1:

Enter radius of Circle 1: 2
Enter radius of Circle 2: 4
Circumference if circle 1: 12.56
Circumference if circle 2: 25.12
Area of circle 1: 12.56
Area of circle 2: 50.24
Circle 2 is bigger than Circle 1
Expected Input/Output 2:

Enter radius of Circle 1: 4
Enter radius of Circle 2: 4
Circumference if circle 1: 25.12
Circumference if circle 2: 25.12
Area of circle 1: 50.24
Area of circle 2: 50.24
Both Circle are Equal
Write the code in script_3/circle.py
