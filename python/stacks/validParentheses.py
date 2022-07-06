def isValid(s):
    stack = []
    map = {
        ')':'(',
        '}': '{',
        ']': '['
    }
    for each in s:
        # if not closing par, add to stack
        if each not in map:
            stack.append(each)
            continue
        if not stack or stack[-1] != map[each]:
            return False
        if stack[-1] == map[each]:
            stack.pop()
        
    return not stack
print(isValid('()('))