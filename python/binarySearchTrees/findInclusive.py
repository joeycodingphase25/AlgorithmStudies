# difficulty:: medium
# O(N) time complexity, O(n) space

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# helper function to clean up the understanding and pass through the initial array
def findInclusiveOnTree(startNode, low, high):
    return help(startNode, low, high, [])

def help(startNode, low, high, resultArray):
    currentNode = startNode
    if currentNode == None:
        return
    if currentNode.value <= high and currentNode.value >= low:
        resultArray.append(currentNode.value)
        # recursively call and pass down newly appended array values
        left = help(currentNode.left, low, high, resultArray)
        right = help(currentNode.right, low, high, resultArray)
    # here we can return resultArray due to the local nature of variables
    return resultArray



node1 = Node(10)
node1.left = Node(5)
node1.left.left = Node(3)
node1.left.right = Node(7)
node1.right = Node(15)
node1.right.right = Node(18)


print(findInclusiveOnTree(node1, 3, 15))