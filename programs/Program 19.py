def twoSum(prices, target):
    seen = {}

    for i in range(len(prices)):
        complement = target - prices[i]

        if complement in seen:
            return [seen[complement], i]

        seen[prices[i]] = i

    return None