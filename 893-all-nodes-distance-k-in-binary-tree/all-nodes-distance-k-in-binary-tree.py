# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)

        curr = root

        def graph(node, parent):
            if node:
                if parent:
                    adj[node.val].append(parent.val)
                    adj[parent.val].append(node.val)
                
                if node.left:
                    graph(node.left, node)
                if node.right:
                    graph(node.right, node)
        graph(root, None)
        queue = deque()
        queue.append((target.val, 0))
        visit = set()
        visit.add(target.val)

        while queue:
            curr, pos = queue.popleft()

            if pos == k:
                return list(set([node for node, dist in queue] + [curr] ))
            
            for next in adj[curr]:
                if next not in visit:
                    queue.append((next, pos +  1))
                    visit.add(next)
        
        return []

        
        