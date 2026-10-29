def removeDuplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


nums = list(map(int, input().split()))
print(removeDuplicates(nums))