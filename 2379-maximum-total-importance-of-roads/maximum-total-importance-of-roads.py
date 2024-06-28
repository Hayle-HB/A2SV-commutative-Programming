class Solution:
    def maximumImportance(self, n, roads):
        freq = [0] * n

       
        for road in roads:
            freq[road[0]] += 1
            freq[road[1]] += 1

        nodes = list(range(n))
        nodes.sort(key=lambda x: freq[x], reverse=True)

        ans = 0
        for i in range(n):
            ans += (n - i) * freq[nodes[i]]

        return ans