n =int(input("Enter a Number: "))

p=1
for i in range(n):
    for j in range(i,n):
        print(p,end=' ')
    p=p+1
    print()


