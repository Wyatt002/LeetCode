class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        return [(len([i for i in nums if i < digit])) for digit in nums]
        