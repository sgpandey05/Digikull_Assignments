"""Set Expected Input/Output:

Add set elements seperated by space: 1 2 3 4
Output Set using set comprehensions: {8, 2, 4, 6}"""


a = list(map(int,input("\nAdd list elements seperated by space: ").strip().split()))[:4]
multiplied_set = {i*2 for i in a }
  
print("Set using set comprehensions:",multiplied_set)