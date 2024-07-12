# Anagram problem

def arg_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


print(arg_anagram("listen", "silent"))
print(arg_anagram("Srihari", "naidu"))


## Write a program to check given string is pallandrome or not

def given_string_pallandrome(s):
    return s == s[::-1]


is_pallandrome = given_string_pallandrome("121")

if is_pallandrome:
    print("Given string is pallandrome")
else:
    print("Given string is not a pallandrome")


# Write a program to reverse a string using O(1) concept.

def reverse_string(s):
    char_list = list(s)
    left, right = 0, len(char_list) - 1

    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left = left + 1
        right = right - 1

    return ''.join(char_list)


print(reverse_string("SrihariNaidu"))


givne_string=input("Given String is Pallandrome?  ")

def is_pall(givne_string):
    converted_one=givne_string.lower()
    return converted_one==converted_one[::-1]

print(is_pall(givne_string))


