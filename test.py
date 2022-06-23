# Takes in two root nodes and returns if BST is same for each node

# Class Structure

class Node():
	def __init__(self):
		self.value = value
		self.left = left
		self.right = right

# Function

firstTree = node1
secondTree = node2

def findDuplicateBST(node1, node2):
	firstTree = node1
	secondTree = node2
	
	while node1.left != None and node1.right != None or node2.left != None and node2.right != None:
		
		# boolean check statement
		if node1.left != node2.left or node1.right != node2.right:
			return False

		# iterate recursively
		
		findDuplicateBST(node1.left, node2.left)
		findDuplicateBST(node1.right, node2,right)

	return True