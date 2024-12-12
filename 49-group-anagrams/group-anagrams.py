class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        for s in strs:
            
            hash[''.join(sorted(s))].append(s)
        
        ans = []

        for a in hash:
            ans.append(hash[a])
        return ans