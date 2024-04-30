# write a program to get current working directory
import os

path_my=os.getcwd()

print(path_my)


# Write a program to create a directory

# os.rmdir("/Users/sriharinaidu/Desktop/WEBAUTOMATION/justcode/OSMOdule/srihari")
# os.mkdir("srihari")

# print(" Directory created")
# os.rmdir("/Users/sriharinaidu/Desktop/WEBAUTOMATION/justcode/OSMOdule/srihari")

# Write a program to list all files

hey_my_files=os.listdir("/Users/sriharinaidu/Desktop/WEBAUTOMATION/justcode/OSMOdule")
print(hey_my_files)

print(" Print All Files in the Console")



print(os.getcwd())
os.chdir("/Users/sriharinaidu/Desktop/WEBAUTOMATION/justcode")
print(os.getcwd())

print(os.listdir())

# rename the file

os.rename("sri.txt","srihari.txt")

print(" Rename successfully..!!")

n = int(input())
mylist = []
for i in range(n):
    mylist.append(i)
print(mylist)

fin=' ' .join()
print(fin)

