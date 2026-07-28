from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 1. Initialize the queue with the root node 'A'
root = TreeNode(
    1,
    TreeNode(5),
    TreeNode(6)
)
queue = deque([root]) 

# 2. Loop until the queue is completely empty
while queue:
    # Remove the first node from the front of the queue
    print([node.value for node in queue])
    current = queue.popleft() 
   
    
    # Add left and right children to the back of the queue
    if current.left:
        queue.append(current.left)
    if current.right:
        queue.append(current.right)
