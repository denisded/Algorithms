def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high)
        guest = list[mid]
        if guest == item:
            return mid
        elif guest > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


a = [3, 6, 2, 5, 7, 12, 1, 9]
print(a)
print(sorted(a))
print(binary_search(sorted(a),5))
