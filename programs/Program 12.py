def hash_func(l,key,n):
    value = key % 10
    if l[value] == None:
        l[value] = key
    else:
        while l[value] != None:
            value = (value + 1) % 10
        l[value] = key
    

l = [None] * 10
n = int(input("Enter number of elements: "))
for i in range(n):
    key = int(input("Enter number: "))
    hash_func(l,key,n)
print("Hash table:")
for i in range(len(l)):
    print(l[i], end=" ")