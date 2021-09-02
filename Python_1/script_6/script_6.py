# numbers = [1, 2, 3, 4, 5]
# Weekdays = [‘Monday’, ‘Tuesday’, ’ Wednesday’, ’ Thursday’, ’ Friday’, ’ Saturday’, ’ Sunday’]
# Num = [‘222’, ’100’, ’85’, ’500’, ’300’]

# 1
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
print()
# 2
num1 = len(numbers)
i=0
while i < num1:
    print(numbers[i])
    i += 1
print()
# 3    
Weeekdays = ['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday']
for Days in Weeekdays:
    print(Days)
print()
#4
wk1 = len(Weeekdays)
i=0
while i < wk1:
    print(Weeekdays[i])
    i += 1
print()
#5
sum = 0
for j in range(0, num1):
    sum = sum + numbers[j]
print("The sum from for loop is {}".format(sum))
print()
# 6
i=0
sum1=0
while i < num1:
    sum1 = sum1 + numbers[i]
    i += 1
print("The sum from While loop is {}".format(sum1))