"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        answer = []

        def dfs(node):
            if not node:
                return []
            
            for ch in node.children:
                dfs(ch)
            
            answer.append(node.val)

        dfs(root)
        return answer
        