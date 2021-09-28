"""
Program to show the use of lambda functions
double = lambda x: x * 2
print(double(5))
Output
10

Part 1:
Write a Python program to count the even, odd numbers in a given array of integers using Lambda. 
Take list as user Input. Hint : filter
Expected Input Output
Add list elements seperated by space 2 3 4 5 6
Number of even numbers in the above array:  3
Number of odd numbers in the above array:  2
"""
# a = list(map(int,input("\nAdd list elements seperated by space: ").strip().split()))[:5]
# def odd_even(num):
#     even_count = 0
#     odd_count = 0
#     for i in num:
#         if i%2 == 0:
#             even_count = even_count+1
#         else :
#             odd_count = odd_count+1
#     print(even_count)
#     print(odd_count)
# odd_even(a) 

a = list(map(int,input("\nAdd list elements seperated by space: ").strip().split()))[:5]
result = list(filter(lambda x: (x % 2 == 0), a)) 
even_count = len(result)
odd_count = len(a) - len(result)
print("Number of even numbers in the above array:  ",even_count)
print("Number of odd numbers in the above array:  ",odd_count)