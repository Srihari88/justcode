n =int(input("Enter a Number: "))

for i in range(n):
    for j in range(i,n):
        print("*", end=' ')
    print()