class MyHashMap:
    def __init__(self):
        self.data = [-1] * 1000001

    def put(self, key, val):
        self.data[key] = val

    def get(self, key):
        return self.data[key]

    def remove(self, key):
        self.data[key] = -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)