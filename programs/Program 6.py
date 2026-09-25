def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

N = int(input("Enter number of products: "))

if N <= 0:
    print("Number of products must be greater than 0.")
else:
    prices = []
    for i in range(N):
        price = float(input(f"Enter price for product {i + 1}: "))
        prices.append(price)

    print(f"\nOriginal Prices: {prices}")

    bubble_sorted = bubble_sort(prices.copy())
    print("\nPrices sorted using Bubble Sort:")
    for price in bubble_sorted:
        print(price)

    selection_sorted = selection_sort(prices.copy())
    print("\nPrices sorted using Selection Sort:")
    for price in selection_sorted:
        print(price)

    insertion_sorted = insertion_sort(prices.copy())
    print("\nPrices sorted using Insertion Sort:")
    for price in insertion_sorted:
        print(price)