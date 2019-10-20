from collections import defaultdict


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        word_count = defaultdict(lambda: 0)
        for i in nums:
            word_count[i] += 1
        ini_len = len(nums)
        processed_len = len(word_count)
        if ini_len == processed_len:
            return False
        return True