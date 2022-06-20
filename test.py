coins = [1,2,5]
def fewest(coins, amount):
    test = sorted(coins)
    i = len(coins)-1
    value = 0
    count = 0
    while i >= 0:
        while (value+coins[i]) <= amount:
            value += coins[i]
            count +=1
            if value == amount:
                return count
        i -= 1
    return False
print(fewest(coins, 11))