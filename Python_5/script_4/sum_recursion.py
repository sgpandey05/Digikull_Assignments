"""Part 2: Write a Python program to add all the elements in a list using recursion
Expected Input/Output:

Add list elements seperated by space 2 3 4 5
14
Update code in script_4/sum_recursion.py"""


arr = list(map(int,input("\nAdd list elements seperated by space: ").strip().split()))[:4]
N = len(arr)

def _findSum(arr, N):
     if len(arr)== 1:
        return arr[0]
     else:
        return arr[0]+_findSum(arr[1:], N)
 
ans =_findSum(arr,N)
print (ans)