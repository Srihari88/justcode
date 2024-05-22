thisdict={

    "name":"Srihari",
    "rollno":45,
    "phoneno":7500705323,
    "Address":"Visakhapatnam"
}

print(thisdict)

print(thisdict['name'])
print(thisdict['rollno'])
print(thisdict['phoneno'])
print(thisdict['Address'])

print(thisdict.keys())
print(thisdict.values())


print(thisdict.items())


for i,j in thisdict.items():
    print(i,j)

thisdict["Study"]="MCA"

print(thisdict)

if "Study123" in thisdict:
    print(" Key is existed on the modal")
else:
    print(" Field not existed on the modal")

thisdict["Study"]="Masters"

print(thisdict)

thisdict.update({"Study":"BSc"})

print(thisdict)

thisdict.pop("Study")
print(thisdict)

thisdict.popitem()

print(thisdict)


del thisdict["phoneno"]

print(thisdict)