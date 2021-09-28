"""
Part 1: Write a Python program to calculate the value of 'a' to the power 'b' using recursion
Expected Input/Output:

Enter the number 6
Enter Power 2
#Output
36
Update code in script_4/power_recursion.py
"""
a =(input("Enter the number :"))
a = int(a)
b =(input("Enter Power :"))
b = int(b)
def power(a,b):
    """This is a recursive function"""
    if b == 1:
	    return a
    else:
	    return (a**b)
obj = power(a,b)
print(obj)