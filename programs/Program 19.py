def twoSum(prices, target):
    seen = {}

    for i in range(len(prices)):
        complement = target - prices[i]

        if complement in seen:
            return [seen[complement], i]

        seen[prices[i]] = i


prices = list(map(int, input().split()))
target = int(input())

print(twoSum(prices, target))