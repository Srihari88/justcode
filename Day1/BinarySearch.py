# Binary Search Algoritham

def binarysearch(arr,target):
    arr.sort()
    left=0
    right=len(arr)-1

    while left<=right:
        mid = (left + right) // 2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return -1

arr=[5,7,3,44,55,99,77,66,55,44]
target=55

result=binarysearch(arr,target)

if result!=-1:
    print(" Element found in the array")
else:
    print(" Element not found in the array")


# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         # Check if the target is equal to the value at the middle index
#         if arr[mid] == target:
#             return mid
#         # If the target is greater, ignore the left half
#         elif arr[mid] < target:
#             left = mid + 1
#         # If the target is smaller, ignore the right half
#         else:
#             right = mid - 1
#
#     # If the target is not found in the array
#     return -1
#
# # Example usage:
# arr = [2, 5, 7, 9, 11, 13, 15, 17, 19]
# target = 130
# result = binary_search(arr, target)
#
# if result != -1:
#     print(f"Element found at index {result}.")
# else:
#     print("Element not found in the array.")
