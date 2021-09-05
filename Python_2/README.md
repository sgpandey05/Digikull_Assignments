# Python-second-Assignment
Python second Assignment

Before starting this project, Make sure you install virtual env in your system using the following steps

Install virtualenv by following the steps
Mac
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate

Windows
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
OR follow this link https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
 
Script 1: Import Statements and Package
 

What is an import?

When a module is imported, Python runs all of the code in the module file. When a package is imported, Python runs all of the code in the package’s init.py file, if such a file exists. All of the objects defined in the module or the package’s init.py file are made available to the importer.
Also, Python imports are case-sensitive. import Spam is not the same as import spam.
Basic Definitions
module: any *.py file. Its name is the file name.
built-in module: a “module” (written in C) that is compiled into the Python interpreter, and therefore does not have a *.py file.
package: any folder containing a file named init.py in it. Its name is the name of the folder.
in Python 3.3 and above, any folder (even without a init.py file) is considered a package
object: in Python, almost everything is an object - functions, classes, variables, etc.
More Details : https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html

Script:

Write a script to get circumference of a circle.
Import math module to get value of pi.
Take radius of circle as input from User
 

Write the code in script_1/circumference.py
 
 

Script 2: File Operations

Files are named locations on disk to store related information. They are used to permanently store data in a non-volatile memory (e.g. hard disk).

When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.

Hence, in Python, a file operation takes place in the following order:
Open a file
Read or write (perform operation)
Close the file


Python has a built-in open() function to open a file
>>> f = open("test.txt") # open file in current directory
>>> f = open("C:/Python38/README.txt") # specifying full path

Closing Files in Python
When we are done with performing operations on the file, we need to properly close the file.
Closing a file will free up the resources that were tied with the file. It is done using the close() method available in Python.
Python has a garbage collector to clean up unreferenced objects but we must not rely on it to close the file.

f = open("test.txt", encoding = 'utf-8')
#perform file operations
f.close()

open method
open method is not entirely safe. If an exception occurs when we are performing some operation with the file, the code exits without closing the file.
A safer way is to use a try...finally block.
try:
f = open("test.txt", encoding = 'utf-8')
#perform file operations
finally:
f.close()

Write:
In order to write into a file in Python, we need to open it in write w, append a or exclusive creation x mode.
with open("test.txt",'w',encoding = 'utf-8') as f:
f.write("my first file\n")


Read:
To read a file in Python, we must open the file in reading r mode.
f = open("test.txt",'r',encoding = 'utf-8')

We can read a file line-by-line using a for loop. This is both efficient and fast.




for line in f:
... print(line, end = '')
...
This is my first file
This file
contains three lines





Part 1:

Read file sample.txt present in the repository and print its content.

Write the code in script_2/file_operation_1.py
 

Part 2:

There is a directory named “numbers” present in the repository. It contains 10 files named from 1.txt , 2.txt, ….., 10.txt.
Take a input from user from 1 to 10. Open file 1.txt and print its contents if the user selects 1. Similarly print contents of 2.txt if user selects 2 and so on
If user selects any other number. Print “Incorrect Input”

Expected Input and Output:
-> Enter a number between 1 and 10: 3
Here are contents for 3.txt:
This is the content of 3rd file printed here
This is the content of 3rd file printed here
This is the content of 3rd file printed here

-> Enter a number between 1 and 10: 15
>> Please select number between 1 and 10

Write the code in script_2/file_operation_2.py
 

Part 3:

Write a script to save data to a file.
Take name of file as an Input from User. Once a user gives a file name. Take data to store in the file from that user and write to file

Expected Input and Output:
Python random.py
Enter the name of file: argo.txt
Enter the contents to be stored in a file: Hello world
A file named argo.txt is created with “Hello world ” as its contents

Write the code in script_2/file_operation_3.py
 

Part 4:

Copy contents of one file to another file. There is a file main.txt stored in the repository. Write a python script which copy contents of main.txt and store it into a new file duplicate.txt. Pass main.txt and duplicate.txt filenames as command line arguments

Expected Input and Output:


$ cat main.txt
Hello world
$ cat duplicate.txt
Error: No such file exists
$ python run.py main.txt duplicate.txt
Copied file contents of main.txt to duplicate.txt
$ cat duplicate.txt
Hello world


Write the code in script_2/file_operation_4.py
 

Script 3: Collections Module

The collection Module in Python provides different types of containers. A Container is an object that is used to store different objects and provide a way to access the contained objects and iterate over them. Some of the built-in containers are Tuple, List, Dictionary, etc. In this article, we will discuss the different containers provided by the collections module.

 

1. Counter

Counter is a subclass of dictionary object. The Counter() function in collections module takes an iterable or a mapping as the argument and returns a Dictionary. In this dictionary, a key is an element in the iterable or the mapping and value is the number of times that element exists in the iterable or the mapping.
 

2. Orderdict

The OrderedDict() function is similar to a normal dictionary object in Python. However, it remembers the order of the keys in which they were first inserted.
 

Part 1:

Create a script that take Input any n numbers and create a dictionary and Orderdict from the input elements as keys and keep their values as 1 if input element is odd number and 0 if input element is even number
Expected Input and output:
 


->python main.py
No, of elements: 5
Input 1 : 2
Input 2 : 8
Input 3 : 1
Input 4 : 3
Input 5 : 9
Dictionary: { 2: 0, 8: 0, 1: 1, 3: 1, 9: 1 }
OrderedDict([(2, 0), (8, 0), (1, 1), (3, 1), (9, 1)])

 


->python main.py
No, of elements: 5
Input 1 : 2
Input 2 : 10
Input 3 : 1
Input 4 : 3
Input 5 : 2
Dictionary: { 2: 0, 10: 0, 1: 1, 3: 1 }
OrderedDict([(2, 0), (10, 0), (1, 1), (3, 1)])



Write the code in script_3/ordered_dict.py
 

DefaultDict:

A DefaultDict is also a sub-class to dictionary. It is used to provide some default values for the key that does not exist and never raises a KeyError.
DefaultDict objects can be initialized using DefaultDict() method by passing the data type as an argument.

Part 2:

Create a script to take input of n numbers. Add these element to list and DefaultDict and display them

Expected Input and Output:


->python main.py
No, of elements: 5
Input 1 : 2
Input 2 : 8
Input 3 : 1
Input 4 : 3
Input 5 : 9
List: [2,8,1,3,9]
OrderedDict: defaultdict(<class 'int'>, {1: 2, 2: 8, 3: 1, 4: 3, 5: 9})



->python main.py
No, of elements: 5
Input 1 : 2
Input 2 : 8
Input 3 : 1
Input 4 : 1
Input 5 : 2
List: [2,8,1,1,2]
OrderedDict: defaultdict(<class 'int'>, {1: 2, 2: 8, 3: 1, 4: 1, 5: 2})

 

Write the code in script_3/default_dict.py
 

ChainMap:

A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.
Example:

from collections import ChainMap
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
#Defining the chainmap
c = ChainMap(d1, d2, d3)
print(c)

Output:
ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})

No Assignment for ChainMap

 

NamedTuple:

A NamedTuple returns a tuple object with names for each position which the ordinary tuples lack. For example, consider a tuple names student where the first element represents fname, second represents lname and the third element represents the DOB. Suppose for calling fname instead of remembering the index position you can actually call the element by using the fname argument, then it will be really easy for accessing tuples element. This functionality is provided by the NamedTuple.

No assignment for NamedTuple


 

Script 4: Json

Python has a built-in package called json, which can be used to work with JSON data.
Script: A json file subjects.json is stored in repository. It contains data of subjects data
Format: {"English": "92","Maths":"90","History":"90"}
Write a python program to read the json file and add the subjects marks for the student

Expected Input and output:


python main.py
Json : {"English": "92","Maths":"90","History":"90"}
Total Marks: 272

 

Write the code in script_4/json_parse.py
 

Script 5: String Operations

Python has a set of built-in methods that you can use on strings.

Part 1:

Write a python script which takes a sentence as Input and performs following actions on them
Capitalize
Lower
Capitalize first letter
Replace all d by h
Replace all o by zm
Find no, of times a occurred
Count no. of letters string has


**Expected Input and Output:**
> Enter a sentence: Hello World
Capitalize : HELLO WORLD
Lower: hello world
Capitalize first letter: Hello world
Replace all d by h: Hello Worlh
Replace all o by zm: Hellzm Wzmrld 
Find no, of times a occurred: 0
Count no. of letters string has: 10


Write the code in script_5/string_1.py
 

Part 2:

Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead.
 


**Expected Input and Output**:
Enter string: hello
Output: helloing
Enter string : willing
Output: willingly


Write the code in script_5/string_2.py
