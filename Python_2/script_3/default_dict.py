'''
Create a script to take input of n numbers. Add these element to list and DefaultDict and display them
Expected Input and Output:

->python main.py No, of elements: 5 Input 1 : 2 Input 2 : 8 Input 3 : 1 Input 4 : 3 Input 5 : 9 
List: [2,8,1,3,9] OrderedDict: defaultdict(<class 'int'>, {1: 2, 2: 8, 3: 1, 4: 3, 5: 9})

->python main.py No, of elements: 5 Input 1 : 2 Input 2 : 8 Input 3 : 1 Input 4 : 1 Input 5 : 2 
List: [2,8,1,1,2] OrderedDict: defaultdict(<class 'int'>, {1: 2, 2: 8, 3: 1, 4: 1, 5: 2})
'''
import os
import collections
from collections import Counter
from collections import defaultdict
from typing import DefaultDict, List, OrderedDict
 
number = int(input("No of elements : "))
list1=[]

for x in range(1, number + 1):
    y = int(input("Input"))
    list1.append(y)
print("\nList : ", list1)
name=list1
mydict=defaultdict(int)
mydict["value"]=list1
print(mydict)

# from collections import defaultdict

# def orderdict(elements):
#     print("List:", elements)

# if __name__ == '__main__':
#     count_of_elements = int(input("Enter no of Elements:"))
#     a = defaultdict(int)
#     elements = []
#     for i in range(1, count_of_elements+1):
#         temp_variable = int(input("Input "+str(i)+":"))
#         elements.append(temp_variable)
#         a[i] = temp_variable
#     orderdict(elements)
#     print("OrederedDict:", a)