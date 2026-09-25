def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


N = int(input("Enter number of elements: "))

if N <= 0:
    print("Number of elements must be greater than 0.")
else:
    elements = []
    for i in range(N):
        val = int(input(f"Enter element {i + 1}: "))
        elements.append(val)

    elements.sort()
    print(f"\nSorted Array: {elements}")
    target = int(input("Enter the element to search for: "))

    result = binary_search(elements, target)

    if result != -1:
        print(f"\nElement {target} found at index {result} (Position {result + 1}).")
    else:
        print(f"\nElement {target} not found in the array.")
