def knapsack(items,capacity):

    total_value = 0
    items.sort(key=lambda x: x[0]/x[1], reverse = True)

    for value,weight in items:
        if capacity == 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight
            print(f"Added item with value: {value} and weight: {weight}")
        else:
            fraction = capacity/weight
            total_value += value*fraction
            print(f"Added item with value: {value*fraction:.2f} and weight: {capacity}")
            capacity = 0
    print(f"Maximum value in Knapsack = {total_value:.2f}")
    print(f"Remaining capacity in Knapsack = {capacity}")

n = int(input("Enter number of elements: "))
items = []
for i in range(n):
    value = int(input("Enter value: "))
    weight = int(input("Enter weight: "))
    item = [value, weight]
    items.append(item)
capacity = int(input("Enter capacity: "))
knapsack(items, capacity)

