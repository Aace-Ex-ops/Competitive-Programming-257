def row_and_column_major(arr):

    print("Row Major Order:")

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")

    print("\nColumn Major Order:")

    for j in range(len(arr[0])):
        for i in range(len(arr)):
            print(arr[i][j], end=" ")

def array_input(rows,cols):
    arr=[]
    for i in range (rows):
        arr.append([0]*cols)
        for j in range (cols):
            arr[i][j] = int(input(f"Enter element for position ({i},{j}): "))

    row_and_column_major(arr)


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))

array_input(rows,cols)