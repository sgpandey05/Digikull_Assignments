"""Part 1: Write a python script to multiply the element with 2 in the array using List Comprehensions
Write the same script using Set and Generator Comprehensions"""
"""
List Expected Input/Output:

Add list elements seperated by space: 1 2 3 4
Output list using list comprehensions: [2, 4, 6, 8]"""

a = list(map(int,input("\nAdd list elements seperated by space: ").strip().split()))[:4]
multiplied_list = [i * 2 for i in a]
print("\nlist using list comprehensions:  ", multiplied_list)