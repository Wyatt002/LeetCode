class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = 0
        l = 0
        counter = defaultdict(int)
        for r in range(len(s)):
            counter[s[r]] += 1
            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest