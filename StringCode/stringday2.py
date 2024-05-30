mystring = "You are working in python programming language"

print(mystring)

print("The length of the string is: ", len(mystring))
print(" The Index of the pythong is: ", mystring.index("python"))
print("The total number of occuerences of of string is: ", mystring.count('a'))
print(mystring.find("language"))

print(mystring.startswith("You"))
print(mystring.endswith("programming"))

print("Lower letters: ", mystring.lower())
print("Upper Letters: ", mystring.upper())

print("Is lower?", mystring.islower())
print("Is upper?", mystring.isupper())

# Slicing in the string

print(mystring[0:])
print(mystring[-30:])
print('Slicing techiniques: ', mystring[0::1])
print(mystring[5:30])
print(mystring[::-1])

# split method in python

list_of_words=mystring.split()
print(list_of_words)

combine=' Sri '.join(list_of_words)
print(combine)

data = "apple,banana,cherry"

man=data.split(',')
print(man)


text = "one1two2three3four"

import re

parts=re.split(r'\d',text)
print(parts)

text = "a1 b2 c3 d4"

part1=text.split()
print(part1)

numbers = [part[1] for part in parts if part[0].isalpha()]
print(numbers)