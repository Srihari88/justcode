def is_palindrome(number):
    sri=str(number)
    s1=sri[::-1]

    return s1==sri

print(is_palindrome(123))
print(is_palindrome(121))

