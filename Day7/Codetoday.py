# Write a program to for fibnochi


def fibonochi(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return n * fibonochi(n - 1)


print(fibonochi(1))


# Write a program to print Pallindrome


def pallindrome(mystring):
    convert_string = mystring.lower()
    if convert_string == convert_string[::-1]:
        print(" Given string is pallindrome")
    else:
        print(" Given string is not a pallindrome")


print(pallindrome("aba"))


# Print prime numbers between 1 to 100


def is_prime(number):
    if number<=1:
        return False
    zip=number ** 0.5

    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True


def print_prime_numbers():
    for num in range(1,100):
        if is_prime(num):
            print(num)


print_prime_numbers()

