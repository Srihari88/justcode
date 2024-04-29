def binary_search(n, item, start, end):
    middle = (start + end) // 2
    if start == end:
        return None
    if n[middle] > item:
        return binary_search(n, item, start, middle)
    elif n[middle] < item:
        return binary_search(n, item, middle + 1, end)
    else:
        return middle


