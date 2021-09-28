"""Part 2: Write the following dictionary
{“a”: 25, “b”:4,”c”:1,”d”:100}
Using Dict Comprehension calculate the square root of the numbers and store it back to the same key

Expected Input/Output:

{'a': 5.0, 'b': 2.0, 'c': 1.0, 'd': 10.0}"""
import math
import math as mt
input_dict = {
    "a":25,
    "b":4,
    "c":1,
    "d":100
}
output_dict = {}
# for var in input_dict.values():
#     output_dict[var] = math.sqrt(var)  
# print("Output Dictionary:",output_dict )
  
dict_using_comp = {var:math.sqrt(var)for var in input_dict.values()}
print("Output Dictionary using dictionary comprehensions:",dict_using_comp)