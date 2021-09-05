'''
Write a python script which takes a sentence as Input and performs following actions on them Capitalize 
Lower Capitalize first letter Replace all d by h Replace all o by zm Find no, of times a occurred Count no. 
of letters string has

Expected Input and Output:

    Enter a sentence: Hello World 
    Capitalize : HELLO WORLD 
    Lower: hello world 
    Capitalize first letter: Hello world 
    Replace all d by h: Hello Worlh 
    Replace all o by zm: Hellzm Wzmrld 
    Find no, of times a occurred:0 
    Count no. of letters string has: 10

'''
sentence = input('Enter a sentence : ')
capital = sentence.upper()
lower = sentence.lower()
# capfirst = sentence[0].title()+sentence[1:]
capfirst1 = sentence.capitalize()
replace = sentence.replace("d","h")
replace1 = sentence.replace("o","zm")
count = sentence.count("o")
length = len(sentence)

print("Capitalize : ",capital)
print("Lower : ",lower)
# print(capfirst)
print("Capitalize first letter : ",capfirst1)
print("Replace all d by h : ",replace)
print("Replace all o by zm : ",replace1)
print("Find no. of times a occurred : ",count)
print("Count no. of letters string has : ",length)