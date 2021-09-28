"""
Generic Expected Input/Output:

Add generic elements seperated by space 1 2 3 4
Output generic list using generic comprehensions: [2, 4, 6, 8]"""


a = list(map(int,input("\nAdd list elements seperated by space: ").strip().split()))[:4]
multiplied_list = (i * 2 for i in a)
print("values using generator comprehensions:", end = ' ')
for var in multiplied_list:
    print(var, end = ' ')