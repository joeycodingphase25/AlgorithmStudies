string = "test this works"

def reverse(str):
    res = ""
    for letter in string:
        res = letter + res
    return res

print(reverse(string))