# Anagram problem

def arg_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


print(arg_anagram("listen", "silent"))
print(arg_anagram("Srihari", "naidu"))


#
