class Solution(object):
    def isPalindrome(self, x):
        res = [num for num in str(x)]
        l, r = 0, len(res) - 1
        while l < r:
            if res[l] != res[r]:
                return False
            else:
                l += 1
                r -= 1
        return True            
        