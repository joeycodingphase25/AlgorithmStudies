
print('5' in '25')

def test(num):
    count = 0
    for x in range(1,num):
        if '5' not in str(x):
            count+=1
    return count


print(test(1000000000))