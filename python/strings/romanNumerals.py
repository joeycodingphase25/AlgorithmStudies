
test = 'IIII'
def romanTranslator(input):
    hashmap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # create temp value holder
    currentValue = 0
    # iterate backwards
    for i in reversed(range(len(input))):
        currentNum = hashmap[input[i]]
        # if the current number is LESS than previous, need some trickery
        if currentValue > currentNum and currentNum != prevNum:
            currentValue -= currentNum
            prevNum = currentNum
        elif currentValue < currentNum or currentNum == prevNum:
            # keep count
            prevNum = currentNum
            currentValue += currentNum
    return currentValue

print(romanTranslator('MCMXCIV'))