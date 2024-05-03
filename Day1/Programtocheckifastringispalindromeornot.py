#Program to check if a string is palindrome or not

myString=input("Enter a String: ")

modified_string=myString.lower()

reversed_string=reversed(modified_string)
final_one="".join(reversed_string)

if modified_string==final_one:
    print(" Given String is a Palindrome")
else:
    print(" Given String is not a Palindrome")

