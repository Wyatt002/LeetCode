class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [l.lower() for l in s if l.isalnum()]
        l, r = 0, len(s) -1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True         