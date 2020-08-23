'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

# A utility function to insert a new node with the given key
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def path_sum_helper(root, sum_given, sum_so_far):
    if root == None:
        return False

    if (root.val + sum_so_far) == sum_given:
        return True

    return path_sum_helper(root.left, sum_given, sum_so_far+root.val) or \
           path_sum_helper(root.right, sum_given, sum_so_far+root.val)

def path_sum(root, sum_given):
    sum_so_far=0
    return path_sum_helper(root, sum_given, sum_so_far)

# Print inoder traversal of the BST
r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

print path_sum(r, 180)
