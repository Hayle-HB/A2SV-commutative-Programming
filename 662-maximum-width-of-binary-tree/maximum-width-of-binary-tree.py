class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        ans = 0
        q = deque([(root, 0)]) 

        while q:
            size = len(q)
            mmin = q[0][1]
            first, last = 0, 0

            for _ in range(size):
                node, curId = q.popleft()
                curId -= mmin  

                if _ == 0:
                    first = curId
                if _ == size - 1:
                    last = curId

                if node.left:
                    q.append((node.left, curId * 2 + 1))
                if node.right:
                    q.append((node.right, curId * 2 + 2))

            ans = max(ans, last - first + 1)

        return ans