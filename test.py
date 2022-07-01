# given root of tree1 and root of tree2 test to see if same


word = "sample"

def wow(word):
    test = ""
    for letter in reversed(word):
        test = letter + test
    return test 


print(wow(word))