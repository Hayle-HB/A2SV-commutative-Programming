class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def traversal(node):
            if not node:
                return 0
            
            left = traversal(node.left)
            right = traversal(node.right)
            
            balance = node.val + left + right - 1
            
            self.moves += abs(balance)
            
            return balance
        
        traversal(root)
        return self.moves