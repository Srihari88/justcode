my_string="Srihari Naidu "

print(my_string[0:8])
print(my_string[::-1])
print(my_string[-6:])

for char in my_string:
    print(char)


print(my_string.upper())
print(my_string.lower())
print(len(my_string))
print(my_string.strip())
print(my_string.split())
print(my_string.count('i'))
print(my_string.index('N'))
print(my_string.title())
print("Boolean value verification",my_string.isalpha())
print(my_string.isascii())
print(my_string.isdecimal())
print(my_string.islower())
print(my_string.isprintable())
print(my_string.isalnum())
print(my_string.isupper())
print(my_string.islower())
print(my_string.isspace())
print(my_string.find("Naidu"))
print(my_string.replace("Naidu","Pudu"))
print(my_string)
print(my_string.center(30,'_'))
print(my_string.ljust(30,'_'))
print(my_string.rjust(30,'_'))

# Join method in the string


join_method='s'.join(my_string)
print(join_method)

# Write a small program to modify the string and concate something inside it

words="Python program is very easy"

word=words.split()
updated_string=[]

print(word)

for each in range(len(word)):
    if each%2==1:
        updated_string.append(word[each].upper())
    else:
        updated_string.append(word[each])
final_string=' '.join(updated_string)
print(final_string)


# Write a program to sort the string



