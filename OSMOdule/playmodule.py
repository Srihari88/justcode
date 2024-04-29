import  os

# os.rename("sri.txt","srihari.py")
#
# print(" File Rename successfully")

os.chdir('/Users/sriharinaidu/Desktop')

for dirpath,dirnames,filenames in os.walk('/Users/sriharinaidu/Desktop'):
    print("Current path",dirpath)
    print(" Directories:",dirnames )
    print("Files", filenames)