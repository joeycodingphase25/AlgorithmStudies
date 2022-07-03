# 0(n) time, O(n) space

# def reverse(num: int) -> int:
#         stringNum = str(num)
#         reverseStringNum = stringNum[::-1]
#         reverseNum = reverseStringNum
#         minSize, maxSize = (2**31) * -1, 2**31
#         if  minSize < int(reverseNum) < maxSize:
#             return int(reverseNum)
#         else:
#             return 0

#0(n) time, O(n) space

num = -123
def reverse(num: int) -> int:
    # pop and divide
    temp = 0
    sign = False
    if num < 0:
        sign = True
        num *= -1
    while num != 0:
        temp *= 10
        temp += num % 10
        num //= 10
    if sign:
        num *= -1
    minSize, maxSize = (2**31) * -1, 2**31
    return temp if minSize < temp < maxSize else 0

# print(reverse(num))



