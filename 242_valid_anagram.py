# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for i in s:
            count[i] += 1
        for i in t:
            count[i] -= 1
        if [n for n in count.values() if n != 0]:
            return False
        return True
    
    # same with solution: return Counter(s) == Counter(t)
    # or: return sorted(s) == sorted(t) (more complexity due to sorting)