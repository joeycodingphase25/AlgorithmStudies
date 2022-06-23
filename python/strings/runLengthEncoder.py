# Difficulty: Easy
# O(n) time, O(n) space


def runLengthEncoding(string):
    test = []
    length = 1
    for i in range(1, len(string)):
        current= string[i]
        prev= string[i-1]
        if current != prev or length==9:
            test.append(str(length))
            test.append(prev)
            length = 0
        length +=1
    test.append(str(length))
    test.append(string[len(string)-1])
    return ''.join(test)