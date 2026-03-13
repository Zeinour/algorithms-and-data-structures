def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


numbers = [4, 2, 7, 1, 9]

result = linear_search(numbers, 7)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
