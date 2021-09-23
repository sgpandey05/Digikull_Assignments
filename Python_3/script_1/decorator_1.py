"""
Part 1 : Create a decorator to print a statement n no. of times.
 n is the number of times you want to print a statement

Example INPUT/OUTPUT 1
What do you want to print?
        Hello World How many times do you want to print the statement? 5 
        #OUTPUT Hello World Hello World Hello World Hello World Hello World
"""
# def dec1(func1):
#     def nowexec():
#         print("What Do You Want to Print ? " )
#         func1()
#     return nowexec

# @dec1
# def name():
#     pri = input()
#     n = int(input("enter no. of times you want to print the statement"))
#     for i in range(0,n):
#         print(pri)
    
# name()

def text_statement(text):
    print(text)


def multiple_print(func):
    def v2(text, count):
        for i in range(count):
            text_statement(text)

    return v2

text = input("What do you want to print?")
count = int(input("How many times do you want to print the statement? "))

text_statement_decorator = multiple_print(text_statement)
text_statement_decorator(text, count)