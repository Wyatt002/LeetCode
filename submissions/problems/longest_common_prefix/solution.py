class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for str in strs:
                if i == len(str) or strs[0][i] != str[i]:
                    return strs[0][:i]
        return strs[0]                