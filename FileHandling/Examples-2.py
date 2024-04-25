# Example-5 declare with statement.


with open("srihari.txt","w") as fh:
    fh.write(" Hello Srihari")
print(fh.closed)



# Example-6 Wanted to read some character of the file.

with open("srihari.txt","r") as fh:
    mydata=fh.read()
    print(mydata)

    # read method will read total data
    # If you wanted to read each chacter you need to pass index

with open("srihari.txt","r") as fh:
    mydata=fh.read(8)
    print(mydata)

# wanted to read the data from specic point.

with open("srihari.txt","r") as fh:
    fh.seek(3)      # Move the cursor
    mydata=fh.read(8)
    print(mydata)

# To read the data

with open("srihari.txt","r") as fh:
    fh.seek(0)
    mydata=fh.readline()
    print(fh.tell())
    print(mydata)



with open("srihari.txt","r") as fh:
    fh.seek(0)
    b=fh.read(5)
    c=fh.read(15)
    print(b)
    print(c)


