# Write a program to write for slicing

sri_string="srihari naidu pudu srihari srihari srihari"

sri_split=sri_string.split()
count=0
for word in sri_split:
    if word in "srihari":
        count+=1

print(count)


# Program to write a compherthence of lists

# noraml flow using for loop
list_numbers=[]
for numbers in range(10):
    list_numbers.append(numbers)
print(list_numbers)

# Enhanced program using the comperhence

values=[number  for number in range(10)]

print("Comperhence List",values)


