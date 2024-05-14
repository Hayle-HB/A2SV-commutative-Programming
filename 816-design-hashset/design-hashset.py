class MyHashSet:

    def __init__(self):
        self.dic = {}

    def add(self, key: int) -> None:
        self.dic[key] = 1

    def remove(self, key: int) -> None:
        self.dic[key] = 0

    def contains(self, key: int) -> bool:
        return self.dic.get(key,0)!=0

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)