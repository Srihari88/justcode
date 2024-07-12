#Write a program about the list comprehension

s = [x1**2 for x1 in range(10)]

print("Squres of Given Numbers",s)


s = [x1 for x1 in range(10) if x1%2==0]
print("Print the list of even numbers",s)


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

final_list=[item for sublist in nested_list for item in sublist]
print("Final List",final_list)

given_string="hello"
upper_case=[i.upper() for i in given_string]
print(upper_case)


words = ["hello", "world", "python", "is", "awesome"]

lengths = [len(word) for word in words]

print(lengths)


s="Devanshi Pudu"

print(s)


s_len=len(s)
print(s_len)


for char in range(s_len):
    print(s[char])