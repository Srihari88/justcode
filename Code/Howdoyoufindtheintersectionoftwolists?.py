def intersection_of_lists(list1,list2):
    f1=set(list1)
    print(f1)
    f2=set(list2)
    print(f2)

    return list(set(list1)&set(list2))

print(intersection_of_lists([1,2,3,4],[3,4,5,6]))