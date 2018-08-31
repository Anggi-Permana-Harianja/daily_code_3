'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

class Node:
	def __init__(self, val, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

left_node = Node('left', Node('left.left'), Node('left.right'))
right_node = Node('right', Node('right.left'), Node('right.right'))
node = Node('root', left_node, right_node)

'''
serialize function, should use BFS in a level by level fashion with queue
'''
serialized_tree = []

def serialize(root):
	
	global serialized_tree

	queue = []

	queue.append(root)
	

	while(len(queue) > 0):
		node = queue.pop(0)
		serialized_tree.append(node.val)
		
		if node.left:
			queue.append(node.left)

		if node.right:
			queue.append(node.right)

	return ' '.join(serialized_tree)

print(serialize(node))

'''
deserialize tree, put serialized_tree back to its origin form as tree
'''

def deserialize(serialized_tree):
	serialized_tree = serialized_tree.split(' ')

	root = Node(serialized_tree.pop(0))
	current_node = root
	
	while len(serialized_tree) > 0:
		subtrees = serialized_tree.pop(0)
		build_tree(root, subtrees)
		
	return root

def build_tree(root, childs):
	pos = childs.split(".")

	current = root

	while pos:
		if pos[0] == 'left':
			if current.left is None:
				current.left = Node(childs)
			else:
				pos.pop(0)
				current = current.left
		else:
			if current.right is None:
				current.right = Node(childs)
			else:
				pos.pop(0)
				current = current.right


print(deserialize(serialize(node)).val)
print(deserialize(serialize(node)).left.val)
print(deserialize(serialize(node)).left.left.val)
print(deserialize(serialize(node)).left.right.val)
print(deserialize(serialize(node)).right.left.val)
print(deserialize(serialize(node)).right.right.val)