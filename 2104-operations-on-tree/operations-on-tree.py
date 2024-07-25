class LockingTree:

    def __init__(self, parent: List[int]):
        self.parents = defaultdict(int)
        self.descendants = defaultdict(list)
        self.locked = defaultdict(int)

        for i in range(len(parent)):
            self.parents[i] = parent[i]
            self.descendants[parent[i]].append(i)

        del self.descendants[-1]
        


    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locked and self.locked[num] == user:
            del self.locked[num]
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        descendents = set()
        q = deque([num])
    
        while q:
            curr = q.popleft()
            for next in self.descendants[curr]:
                if next in self.locked:
                    descendents.add(next)
                q.append(next)
       
        if not descendents:
            return False

        parent = self.parents[num]
        while parent != -1 and parent not in self.locked:
            parent = self.parents[parent]
        if parent != -1:
            return False
        
        for next in descendents:
            del self.locked[next]
        self.locked[num] = user
        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)