from collections import defaultdict


class Solution:
    def majorityElement(self, nums: [int]) -> int:
        word_count = defaultdict(lambda: 0)
        for i in nums:
            word_count[i] += 1
        word_count = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))
        return list(word_count.keys())[0]


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 3, 1, 1]
    print(s.majorityElement(arr))