# Python-fourth-Assignment


Inheritance is used to indicate that one class will get most or all of its features from a parent class.
It refers to defining a new class with little or no modification to an existing class. The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.

Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

Python Inheritance Syntax
class BaseClass: 
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
The derived class inherits features from the base class where new features can be added to it. This results in the re-usability of the code.

Example 1:
class Parent(object): 
	def implicit(self):
		print("PARENT implicit()")
class Child(Parent):
	pass 

dad = Parent();
son = Parent
dad.implicit() 
son.implicit() 


> python script.py 
PARENT implicit() 
PARENT implicit() 
Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.
As we know, a child class inherits all the methods from the parent class. However, you will encounter situations where the method inherited from the parent class doesn't quite fit into the child class. In such cases, you will have to re-implement method in the child class. This process is known as Method Overriding.
In you have overridden a method in child class, then the version of the method will be called based upon the the type of the object used to call it. If a child class object is used to call an overridden method then the child class version of the method is called. On the other hand, if parent class object is used to call an overridden method, then the parent class version of the method is called.

Examples 2:
class Parent(object): 
	def implicit(self):
		print("PARENT implicit()")
class Child(Parent):
	def override(self):
	print "CHILD override()" 
dad = Parent();
son = Parent
dad.implicit() 
son.implicit()

>python script.py 
PARENT override() 
CHILD override() 
Assignment:
Consider you are developing software for managing a Zoo. The Zoo has 5 types of animals: Lion, Tiger, Giraffe, Elephant, deer
Create a Parent Animal class and 5 child classes -> Lion, Tiger, Giraffe, Elephant, deer
Each Animal has these 4 properties

Name
Category. Eg. Mammal
The food they love to eat
The noise that animals make
Each Animal do the following functions in the zoo which would be methods in the zoo

Feed Food. ie. feed_food() -> print what that animal eats
Make noise i.e make_noise() -> print noise made by that animal
Where
Now create a class Zoo. Create a list animal_list to maintain a list of animals that will be added to Zoo

Create a method add_animal which will add Animal Object to the animal_list of the zoo
After Defining all the classes. Following will be the actions that need to be performed
Add 2 lions, 1 Tiger, 3 Giraffe, 1 Elephant, 1 deer
Add these Animals to the Zoo
Feed all the animals.
Print Voice made by all animals
Expected Input/Output:

Enter count of Lions:
2
Enter the name of Lion 1: L1
Enter the category of Lion 1: carnivorous
Enter Noise made by Lion 1: RaaaR
Enter Food Loved by Lion 1: Meat

Enter the name of Lion 2: L2
Enter the category of Lion 2: carnivorous
Enter Noise made by Lion 2: RoooR
Enter Food Loved by Lion 2: chicken

Enter the count of Tiger:
1
Enter the name of Tiger 1: T1
Enter the category of Tiger 1: carnivorous
Enter Noise made by Tiger 1: Gaw
Enter Food Loved by Tiger 1: chicken

Enter the count of Giraffe:
3
Enter the name of Giraffe 1: G1
Enter the category of Giraffe 1: herbivores
Enter Noise made by Giraffe 1: oooooo
Enter Food Loved by Giraffe 1: Big Leaves

Enter the name of Giraffe 2: G2
Enter the category of Giraffe 2: herbivores
Enter Noise made by Giraffe 2: ohohohoh
Enter Food Loved by Giraffe 2: Big Leaves

Enter the name of Giraffe 3: G3
Enter the category of Giraffe 3: herbivores
Enter Noise made by Giraffe 3: ooooh
Enter Food Loved by Giraffe 3: small Leaves

Enter count of Elephant: 
1
Enter the name of Elephant 1: E1
Enter the category of Elephant 1: herbivores
Enter Noise made by Elephant 1: trumpet
Enter Food Loved by Elephant 1: Fruits

Enter count of Deer: 
2
Enter the name of Deer 1: D1
Enter the category of Deer 1: herbivores
Enter Noise made by Deer 1: bleet
Enter Food Loved by Deer 1: Grass

Enter the name of Deer 2: D2
Enter the category of Deer 2: herbivores
Enter Noise made by Deer 2: bellow
Enter Food Loved by Deer 2: Fruits
#Output

Zoo Animals Dictionary: {“L1”: ”carnivorous”, ”L2”: ”carnivorous”, “T1”: ”carnivorous”, “G1”: ”herbivores”, ”G2”:  ”herbivores”, “G3”:  “herbivores”, “E1”: ”herbivores”, “D1”: ”herbivores”, “D2”: “herbivores”}
Food:
L1: meat
L2: chicken
T1: chicken
G1: Big Leaves
G2: Big Leaves
G3: small Leaves
E1: Fruits
D1: Grass
D2: Fruits
Voices:
L1: RaaaR
L2: RoooR
T1: Gaw
G1: oooooo
G2: ohohohoh
G3: ooooh
E1: trumpet
D1: bleet
D2: bellow
