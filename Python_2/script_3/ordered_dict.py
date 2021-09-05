import os
import collections
from collections import Counter
from typing import OrderedDict

# number = int(input("No of elements : "))
# myDict = {}

# for x in range(1, number + 1):
#     if (x % 2) == 0:
#         myDict[x] = 0
#     else:
#         myDict[x] = 1

# ODic = OrderedDict(myDict)  
# print("\nDictionary : ", myDict)
# print("\nOrderedDict : ", ODic)

number = int(input("No of elements : "))
myDict = {}

for x in range(1, number + 1):
    y = int(input("Input"))
    if (y % 2) == 0:
        myDict[y] = 0
    else:
        myDict[y] = 1

ODic = OrderedDict(myDict)  
print("\nDictionary : ", myDict)
print("\nOrderedDict : ", ODic)