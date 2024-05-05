def remove_duplicates_from_list(number):
    return list(set(number))

input_list=[1,2,3,4,2,3,4,5,4,6,7,7,6]

result=remove_duplicates_from_list(input_list)

print("Original List:", input_list)
print("List with Duplicates Removed:", result)