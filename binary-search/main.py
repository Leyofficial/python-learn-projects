def binary_search(arr, target):
    left, right = 1, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]
        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


arr = list(range(1, 101))
target = int(input("Enter a number to search in the list from 1 to 100: "))
result = binary_search(arr, target)
if result != -1:
    print(f"The number {target} was found in the list at position {result}.")
else:
    print(f"The number {target} was not found in the list.")
