class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        self.max_depth = 0
        
        def dfs(node, depth):
            if not node:
                return
            depth += 1
            if not node.children:
                self.max_depth = max(self.max_depth, depth)
                return
            
            for child in node.children:
                dfs(child, depth)
        
        dfs(root, 0)
        return self.max_depth
