from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def breadth_first_search(root):
    """Returns tree values in level order."""
    if not root: return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return result
