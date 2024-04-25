"""

Two types of files
1. binary files : mp3 files, pdg, video files,audio files
2. text files: txt, .c,.java

1. Open file using open() function
2. read or write operation:
    read(),
    readline(),
    readlines(),
    write(),
    write()
3. Once all operations completed, close the file.

Note: The default operations is read()


Modes in File Handling :
    1. r: read mode
    2. w: write mode
    3. a: append mode

the deault operations mode is : read
to read data file is mandatory

"""

#Example-1: Create file and write the data.
f=open("sample.txt","w")
f.write("Hey..!! How are you..!")
f.close()
print(" Operation is completed.")

# Example-2: Read the data from file

f=open("sample.txt","r")
data=f.read()
print(data)
f.close()
print(" Connection closed")

# Example-3: Append the data

f=open("srihari.txt","a")
f.write("\ Hello Good morning Srihari Naidu")
f.close()
print(" Operations are completed")

# Example-4:

f=open("sample.txt","w")
print(f)
print(f.name)
print(f.mode)
print(f.closed)
f.close()
print(f.closed)
