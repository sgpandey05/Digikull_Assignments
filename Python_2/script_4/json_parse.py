'''
Script 4: Json

Python has a built-in package called json, which can be used to work with JSON data. Script: A json file subjects.json is stored in repository. It contains data of subjects data Format: {"English": "92","Maths":"90","History":"90"} Write a python program to read the json file and add the subjects marks for the student

Expected Input and output:

python main.py Json : {"English": "92","Maths":"90","History":"90"} Total Marks: 272
'''
'''doubt

'''
import json

with open('/home/shivam/DigiKull Assignments/Python2/python-second-assignment-sgpandey05-main/subjects.json') as f:
    data = json.load(f)
print(data)
values = []
for key,value in data.items():
    values.append(int(value))
total = sum(values) #Compute sum of the values.
print('Total marks is: {}'.format(total))

# value = list(map(lambda key: int(json_string[key]), json_string))
#     print("Total Marks:", sum(value))