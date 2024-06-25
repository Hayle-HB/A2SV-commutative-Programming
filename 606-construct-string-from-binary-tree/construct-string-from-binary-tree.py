class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left = None
        self.right = right = None

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        stack = [root]
        visited = set()
        ans = []

        while stack:
            node = stack[-1]
            
            if node in visited:
                stack.pop()
                ans.append(")")
            else:
                visited.add(node)
                ans.append("(" + str(node.val))
                
                if node.left is None and node.right is not None:
                    ans.append("()")
                
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return "".join(ans)[1:-1]