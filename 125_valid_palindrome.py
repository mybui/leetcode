# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

# Solution 1: compare reverse string
# Solution 2: using two pointers at the beginning and the end

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        # Remove any non-alphanumeric characters and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        
        # Reverse string and check if the string is equal to its reverse
        return s == s[::-1]
    
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        # Remove any non-alphanumeric characters and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        
        # Place 2 pointers at the beginning and the end
        i, j = 0, len(s)-1
        # as long as the 1st pointer is smaller than the 2nd pointer
        while i < j:
            # check if they are equal
            # or immediately return False
            if s[i] != s[j]:
                return False
            i, j = i+1, j-1
        return True