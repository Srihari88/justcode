import os
# os.rename("srihari.txt","sri.txt")
# print(" OOperation completed")



# Write a program to create a file , add data, write data, rename file and remove file


f=open("hosi.txt","w+")
f.write("Hey, How are you Hosi  \n Are you going to shcool ")
os.rename("hosi.txt","Hansi.txt")
print(" Operation completed")
os.remove("Hansi.txt")
print(" File removed successfully")



# write a program to create directory

os.mkdir("srihari")
os.chdir("srihari")
print(os.getcwd())
os.rmdir("srihari")
print("Operations completed")
