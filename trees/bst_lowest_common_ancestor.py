"""
Lowest common ancestor in a binary search tree.
Utilising the fact that all nodes to the left are smaller than the parent and nodes to right are larger than the parent.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if p.val < root.val and q.val < root.val:
        return self.lowest_common_ancestor(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return self.lowest_common_ancestor(root.right, p, q)
    else:
        return root
