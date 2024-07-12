#Write a program to print every second word in capital letters

my_string="Hello good morning everyone"
my_string.swapcase()

addone=[]

splitone=my_string.split()

for i in range(len(splitone)):
    if i%2==0:
        addone.append(splitone[i])
    else:
        addone.append(splitone[i].upper())

reveresed_one=' '.join(addone)
print(reveresed_one)


#Write the same program using the list Comperhension

saveone=[splitone(li).upper() for li in range(len(splitone)) if li%2==0]

print(saveone)




for i in range(0,10):
    print(i)


value=[i*9 for i in range(0,10)]
print(value)


words=[i.upper() for i in "Srihari Naidu"]

print(words)


# Even Numbers

numbers=[even for even in range(20) if even%2==0]
print(numbers)

# Upper case words

words_list=[" Python","Is", "Easy", "Language"]

many=[words_list.upper() for words_list in words_list ]

print(many)

# Can you print list of each element in the given nested list
my_nested_list=[[5,6,7],[87,4,5],[23,9,8]]

hey=[x for nest in my_nested_list for x in nest]
hey.sort()
print(hey)


words_list=[" Python","Is", "Easy", "Language"]

word_length=[len(word_len) for word_len in words_list]

print(" Length of each word",word_length)


numbers = [1, 2, 3, 4, 5]


lab_one=["Even" if num%2==0 else "Odd" for num in numbers]
print(lab_one)


# Extract unique characters from a list of strings
strings = ["hello", "world", "python"]

unique={c for string in strings for c in string}
print(unique)


# Extract vowels from a list of strings
strings = ["hello", "world", "python"]


sri=[v for vow in strings for v in vow if v in "aeiou"]
print(sri)



for i in range(0, 10):
    print(i)


value=[i for i in range(0,10)]

print(value)
