# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        answer = []
        queue = [root]

        while queue:
            level = []
            next_queue = []
            for node in queue:
                level.append(node.val)
                if node.children:
                    next_queue.extend(node.children)
            answer.append(level)
            queue = next_queue

        return answer
