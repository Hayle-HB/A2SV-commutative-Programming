# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
            first = second = prev = None
            
            current = root
            while current:
                if current.left is None:
                    # Process current node
                    if prev and prev.val > current.val:
                        if first is None:
                            first = prev
                        second = current
                    prev = current
                    current = current.right
                else:
                    # Find the inorder predecessor of current
                    pre = current.left
                    while pre.right and pre.right != current:
                        pre = pre.right
                    
                    if pre.right is None:
                        # Establish link from predecessor to current
                        pre.right = current
                        current = current.left
                    else:
                        # Remove the link
                        pre.right = None
                        # Process current node
                        if prev and prev.val > current.val:
                            if first is None:
                                first = prev
                            second = current
                        prev = current
                        current = current.right
            
            # Swap the values of the first and second nodes to correct the BST
            if first and second:
                first.val, second.val = second.val, first.val
                
