# Writing the bubble sort program


def bubble_sort(array):
    swapped = False
    # looping the statements
    for i in range(0,len(array)):

        # looping through second element
        for j in range(0,len(array)-1-i):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]= temp
        swapped = True

        if not swapped:
            break

data = [-2, 45, 0, 11, -9]

bubble_sort(data)

print(data)
