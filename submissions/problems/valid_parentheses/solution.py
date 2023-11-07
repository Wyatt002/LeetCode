class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for char in s:
            if char in map:
                stack.append(map[char])
            elif not stack or char != stack.pop():
                return False
        return not stack