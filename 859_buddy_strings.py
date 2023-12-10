# https://leetcode.com/problems/buddy-strings/description/

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # 1. if lengths unequal
        # return False immediately
        if len(s) != len(goal):
            return False

        # 2. if lengths equal
        # 2.1. if exact same strings, check if it's possible to swap
        # (is there any duplicated letters)
        if s == goal and len(set(s)) < len(s):
            return True

        # 2.2. if different strings
        # get a list of different letters
        # return True if length of list = 2 (because ONLY need to swap 2 letters)
        # and swap successfully
        pairs = [(a, b) for a, b in zip(s, goal) if a != b] # e.g. 
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]