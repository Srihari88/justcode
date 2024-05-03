# Print the program to even numbers from 0 to 50


even=[]

for number in range(50):
    if number%2==0:
        even.append(number)

print(even)

# Write same program using comprehensions

mynum=[number for number in range(50) if number%2==0]
print(mynum)


# write a program strings that starts with 'a' and ends with 'y'

my_string=["any","albany","apple","world","hello",""]

validated_strings=[]

for hey_strings in my_string:
    if len(hey_strings)<=1:
        continue
    if hey_strings[0]!="a":
        continue

    if hey_strings[-1]!="y":
        continue

    validated_strings.append(hey_strings)

print(validated_strings)


validated_str=[hey_strings
                for hey_strings in my_string
                if len(hey_strings)>=2
                if hey_strings[0]=='a'
                if hey_strings[-1]=='y']

print("Comperhension ",validated_str)


# Write a program to Flattening a matrix (List of lists)

matrix=[[1,2,4],[4,5,6],[7,8,9]]

flattend=[]

for row in matrix:
    for eachone in row:
        flattend.append(eachone)

print(flattend)

finalone=[eachone for row in matrix  for eachone in row]

print(finalone)


# write a program to categorize even or odd
categorize=[]

for i in range(20):
    if i%2==0:
        categorize.append("Even")
    else:
        categorize.append("Odd")

print(categorize)

# Write the same program using the Comperhension

catr=["Even" if i%2==0 else "Odd" for i in range(20)]
print(catr)


# Adding few more examples...

# Example-1: Print numbers from 1 to 2 with multiple of 2

eachtwo=[x*2 for x in range(20) ]
print(eachtwo)

# Example-2: Write a program to print every second character as a Capital letter

everysecond=[char.upper() for char in "Srihari" ]
print(everysecond)

# Example-3: Write a program to print every second word should be capital

anyotheroption="srihari naidu pudu kori"

addone=[]
splitone=anyotheroption.split(' ')
for wordcount in range(len(splitone)):
    if wordcount%2!=0:
        addone.append(splitone[wordcount].upper())
    else:
        addone.append(splitone[wordcount])

print(' '.join(addone))


# Write the same above program using List Comperhension




