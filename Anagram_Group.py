from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            print(tuple(sorted(s)))
            ans[tuple(sorted(s))].append(s)
        return ans.values()


a = ['zxy','bac']
s = Solution()

print(s.groupAnagrams(a))