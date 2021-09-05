'''
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead.

Expected Input and Output: 
Enter string: hello 
Output: helloing 
Enter string : willing 
Output: willingly

Write the code in script_5/string_2.py
'''

enter =  input("Enter string : ")

if "ing" in enter:
    output = enter.replace("ing","ly")
else:
    output = enter+"ing"
print("Output : ",output)