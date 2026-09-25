n = int(input("Enter the number of elements: "))

if (n<=0):
    print("Number of elements must be greater than 0.")

else:
    flag = -1
    list = []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        list.append(val)
    target = int(input("Enter the target sum: "))
    for i in range(n):
        for j in range(i+1, n):
            if list[i] + list[j] == target:
                print(f"Pair found: ({i}, {j})")
                flag = 1
                break
    if not flag:
        print("No pair found")