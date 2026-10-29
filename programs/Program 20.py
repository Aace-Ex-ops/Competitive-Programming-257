def isValid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)

        else:
            if not stack:
                return False

            if stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


s = input()
print(isValid(s))