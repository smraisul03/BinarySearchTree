class TreeNode:

    # Initialize
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.content = None

    # Insert function
    def insert(self, value, content=None):
        # If value is less than current node, create new node
        if value < self.value:
            # If value is none, set the value as the left node value, otherwise insert the new left value
            if self.left is None:
                self.left = TreeNode(value)
                self.left.content = content
            else:
                self.left.insert(value, content)
        # Value check on the right side of the node
        else:
            # If value is none, set the value as the right node value, otherwise insert the new right value
            if self.right is None:
                self.right = TreeNode(value)
                self.right.content = content
            else:
                self.right.insert(value, content)

    # In-order Traversal Function
    def inOrderTraversal(self):
        # If it is a left node, traverse
        if self.left:
            self.left.inOrderTraversal()
        print(self.value)
        # If it is a right node, traverse
        if self.right:
            self.right.inOrderTraversal()
        print(self.value)

    # Pre-Order Traversal Function
    def inPreOrderTraversal(self):
        # Print the value first, instead of in order
        print(self.value)
        # If it is a left node, traverse
        if self.left:
            self.left.inPreOrderTraversal()
        # If it is a right node, traverse
        if self.right:
            self.right.inPreOrderTraversal()

    # Post-Order Traversal Function
    def inPostOrderTraversal(self):
        # If it is a left node, traverse
        if self.left:
            self.left.inPreOrderTraversal()
        # If it is a right node, traverse
        if self.right:
            self.right.inPreOrderTraversal()

        # Print the value last, instead of first
        print(self.value)

    # Find Specific value of the traversal node
    def find(self, value):
        # If head value is greater, find the left node
        if value < self.value:
            if self.value is None:
                return None
            else:
                return self.left.find(value)
        # If head value is less, find the right node
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        # Else, return true
        else:
            return self


# Initialize Binary
tree = TreeNode(6)

# Inserting functions
tree.insert(1, {"data":  "Hello"})
tree.insert(2, {"data":  "World"})
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)

print('----')
# Find the in order traversal of the binary tree
tree.inOrderTraversal()
print('----')
# Find the pre order traversal of the binary tree
tree.inPreOrderTraversal()
print('----')
# Find the post order traversal of the binary tree
tree.inPostOrderTraversal()
print('----')
# Find the Node 2, with the content associated
print(tree.find(2).content['data'])
