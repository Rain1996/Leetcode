class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for index, n in enumerate(nums):
            nums_dict[n] = index

        result = []
        for index, n in enumerate(nums):
            rest = target - n
            if rest in nums_dict and nums_dict[rest] != index:
                result = [index, nums_dict[rest]]
                break

        return result
