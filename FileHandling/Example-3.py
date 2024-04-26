#Example-3
"""
r+---> Open the file both read and write, File is mandatory
w+--->
a+
"""

#Example-1:

f=open("srihari.txt","r+")
print(f.read())
f.close()
print(" File operation completed")

f=open("srihari.txt","r+")
f.write(" Hello Hanshi, how are you")
f.close()
print(" File operation completed")


# f=open("nofile.txt","r+")
# f.write(" Hello Hanshi, how are you")
# f.close()
# print(" File operation completed")

"""

    If file is not avaliable we will get error message
    f=open("nofile.txt","r+")
      ^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'nofile.txt'
"""


# Examples-2, w+: Both read and write opening, file is optional

f=open("nofile.txt","w+")
f.write(" Hello Hanshi, how are you")
print(f.read())
f.close()
print(" File operation completed")


# Example-3

"""
a+ File is optional 
"""

f=open("nofile.txt","a+")
print(f.read())
f.close()
print(" File operation completed")



# Example-4

f1=open("nofile.txt","r")
f2=open("srihari.txt","w")

for x in f1:
    print(x)
f1.close()
f2.close()

