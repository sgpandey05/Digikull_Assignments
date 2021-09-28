"""Part 2: Write a Python program to add two given lists using lambda. Hint : Map
nums1 = [1, 4, 5, 6, 5]
nums2 = [3, 5, 7, 2, 5]

Expected Input Output

Result: after adding two list
[4, 9, 12, 8, 10]
Update code in script_2/lambda_2.py"""

nums1 = [1, 4, 5, 6, 5]
nums2 = [3, 5, 7, 2, 5]
result = map(lambda x, y: x + y, nums1, nums2)
print(list(result))
