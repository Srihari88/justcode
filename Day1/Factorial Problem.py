# Write a Program to print the factorial

def factorial(x):
    if x==1:
        return 1
    elif x==0:
        return 0
    else:
        return (x*factorial(x-1))

result=factorial(0)
print("Factorial value: ",result)