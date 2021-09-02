# Digikull_Assignments
Assignments 

In programming, a variable is nothing more than a name for something so you can use the name rather than the something as you code. Programmers use these variable names to make their code read more like English and because they have lousy memories. If they didn’t use good names for things in their software, they’d get lost when they tried to read their code again.

underscore in the variable name: We use this character a lot to put an imaginary space between words in variable names.
Script 1: variables

Refer script_1/script_1_sample.py and write a script to list count of each animal in the Forest and also categorize them in Herbivorous and carnivorous and print their count. List of animals shown below
Lion =2
White Tiger=2
red deer=50
elephant=10
spider monkey=100
zebra=17
rhinoceroses=10
Black Panther=10
Harpy Eagles=12
White backed vulture=5
Herbivorous are 3,4,5,6,7
Carnivorous are 1,2,8,9,20

Expected Output:

There are 2 Lions
There are 2 White Tigers
There are 50 Red deers
There are 10 Elephants
There are 100 spider monkeys
There are 17 zebras
There are 10 rhinoceroses
There are 10 Black Panthers
There are 12 Harpy Eagles
There are 5 White-backed vultures
There are total <> Herbivorous animals
There are total <> Herbivorous animals

Note: <> is to be replaced with the addition of animal counts
Write the code in script_1/script_1.py
Script 2. Strings

A string is usually a bit of text you want to display to someone or “export” out of the program you are writing. Python knows you want something to be a string when you put either " (doublequotes) or ' (single- quotes) around the text. You saw this many times with your use of print when you put the text you want to go to the string inside " or ' after the print.
Then Python prints it. Strings may contain the format characters you have discovered so far. You simply put the formatted variables in the string, and then a % (percent) character, followed by the variable. The only catch is that if you want multiple formats in your string to print multiple variables, you need to put them inside ( ) (parentheses) separated by , (commas). It’s as if you were telling me to buy you a list of items from the store and you said, “I want milk, eggs, bread, and soup.” Only as a programmer we say, “(milk, eggs, bread, soup).”

Write a script to do the following:
With one print statement to print all months in a year name each in one line. Hint: use \n escape sequence
Wiy one Print statement all days in a Week in one single line separated by Comma. Hint use formatter to print
With one print statement and not using any escape sequence print number 1 to 10 one below each other. Hint: Use """ to print

Note: You can only use 3 print statements in this assignment

Expected output:
January
February
March
April
May
June
July
August
September
October
November
December
Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
1
2
3
4
5
6
7
8
9
10

Write code in file script_2/script_2.py
Script 3: List, tuple, Boolean;

A list is exactly what its name says—a container of things that are organized in order. It’s not complicated; you just have to learn a new syntax. First, there’s how you make a list:
hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

A tuple is created by placing all the items (elements) inside parentheses (), separated by commas. The parentheses are optional, however, it is a good practice to use them.
A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).

The Python Boolean type is one of Python’s built-in data types. It’s used to represent the truth value of an expression. For example, the expression 1 <= 2 is True, while the expression 0 == 1 is False.


Script
In a list, Add all days in a week into a list and print them
Similarly add all the days in a week in a tuple and print them
Print True or false for following mathematical expressions:
1<2
99>=8
345678+77777<66666-90
7896*5555 == 8989898

Expected Output:
[‘Monday’, ‘Tuesday’,’Wednesday’,’Thursday’,’Friday’,’Saturday’,’Sunday’]
("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
True
True
False
False

Write code in file script_3/script_3.py
Script 4: Input

Up until now, our programs were static. The value of variables was defined or hardcoded into the source code.

To allow flexibility, we might want to take the input from the user. In Python, we have the input() function to allow this. The syntax for input() is:

input([prompt])

where prompt is the string we wish to display on the screen. It is optional.

            num = input('Enter a number: ')
            Enter a number: 10
            num
            '10'

This prompts the user with “Enter a number:?” and puts the result into the variable num. This is how you ask someone a question and get the answer.

Script: Write a python script to ask Argo his age, height, weight and calculate his BMI

The Body Mass Index (BMI) or Quetelet index is a value derived from the mass (weight) and height of an individual, male or female. The BMI is defined as the body mass divided by the square of the body height and is universally expressed in units of kg/m2, resulting from the mass in kilograms and height in meters. The formula is:

BMI = round(weight/ (height * height), 1)
where,
mass or weight is in Kg,
height is in meters

Expected Output:

    Hi Argo, What is your Age?
    27
    What is your Weight in Kg?
    65
    What is your Height in metres?
    1.79
    The BMI is 20.2 -> #Return statement

Write code in file script_4/script_4.py Add Logic in bmi_script_4 function and return the output
Script 5: If else Ternary

Decision-making is required when we want to execute a code only if a certain condition is satisfied.
if test expression:
Body of if
else:
Body of else

The if…elif…else statement is used in Python for decision making.

if test expression:
Body of if
elif test expression:
Body of elif
else:
Body of else
Refer: https://www.programiz.com/python-programming/if-elif-else

Script:
Using the above BMI Script. Ask the User his name and then use of their name to ask their weight and height.
Based on Output of BMI Index, tell the user if they are underweight, healthy, overweight, or Obese

BMI Weight status
Below 18.5 underweight
18.5-24.9 normal
25.0-29.9 overweight
30.0 + obese

Expected Output 1:

    What is your Name:
    Argo
    Hi Argo, What is your Height in metres?
    1.79
    What is your weight:
    65
    Your BMI is 20.2 which means you are healthy. -> #Return statement


Expected Output 2:

    What is your Name:
    Rahul
    Hi Rahul, What is your height:
    1.70
    What is your weight:
    88
    Your BMI is 30.5 which means you are obese. -> #Return statement

Write code in script_5/script_5.py
Add Logic in bmi_script_5 function and return the output
Script 6: Loops

Relation of loops with lists:
You should now be able to do some programs that are much more interesting. If you have been keeping up, you should realize that now you can combine all the other things you have learned with if- statements and boolean expressions to make your programs do smart things.
However, programs also need to do repetitive things very quickly. We are going to learn for loops in this exercise to build and print lists.
The best way to do this is with a list. A list is exactly what its name says—a container of things that are organized in order.

What you do is start the list with the [ (left bracket), which “opens” the list. Then you put each item you want in the list separated by commas, just like when you did function arguments.
Lastly, you end the list with a ] (right bracket) to indicate that it’s over. Python then takes this list and all its contents and assigns them to the variable.

Script:
Create these 3 lists:
numbers = [1,2,3,4,5]
Weekdays = [‘Monday’, ‘Tuesday’,’ Wednesday’,’ Thursday’,’ Friday’,’ Saturday’,’ Sunday’]
Num = [‘222’,’100’,’85,’500’,’300’’]

Print numbers in list ‘numbers’ one below the others using a for loop
Print numbers in list ‘numbers’ one below the others using a while loop
Print the days of the week from list ‘Weekdays’ using For loop
Print the days of the week from list ‘Weekdays’ using the While loop
Calculate the sum of all numbers in the array Num using for loop
Calculate the sum of all numbers in the array Num using while loop

Expected Output:
1
2
3
4
5

1
2
3
4
5

Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday

Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday

The sum from for loop:1207
The sum from while loop:1207

Write code in script_6/script_6.py
Script 7: Command Line

Command line arguments are simply arguments that are specified after the name of the program in the system's command line, and these argument values are passed on to your program during program execution.
Python sys module stores the command line arguments into a list, we can access it using sys.argv. This is very useful and simple way to read command line arguments as String. Let’s look at a simple example to read and print command-line arguments using python sys module.

Example: test.py
import sys

print(type(sys.argv))
print('The command line arguments are:')
for i in sys.argv:
print(i)
Output:

    Python test.py 1 2 3 4 5
    The command line arguments are:
    1
    2
    3
    4
    5


**Script**: Modify the same BMI script which you wrote in “Script 5”
Replace Input type of name, weight and Height from user input to command Input

Expected Output 1:

    python bmi.py Argo 1.79 65
    Name: Argo
    Height: 1.79
    Weight 65
    Your BMI is 20.2 which means you are healthy.


Expected Output 2:

    python bmi.py Rahul 1.7 88
    Name: Rahul
    Height: 1.7
    Weight 88
    Your BMI is 30.5 which means you are obese.

Write code in script_7/script_7.py
