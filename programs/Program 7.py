def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  


N = int(input("Enter number of elements: "))

if N <= 0:
    print("Number of elements must be greater than 0.")
else:
    elements = []
    for i in range(N):
        val = int(input(f"Enter element {i + 1}: "))
        elements.append(val)

    print(f"\nArray: {elements}")
    target = int(input("Enter the element to search for: "))

    result = linear_search(elements, target)

    if result != -1:
        print(f"\nElement {target} found at index {result} (Position {result + 1}).")
    else:
        print(f"\nElement {target} not found in the array.")
