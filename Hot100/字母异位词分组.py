# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：
#
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
from copy import deepcopy
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        length = len(strs)
        dcp = deepcopy(strs)
        dcp = list(map(lambda x: ''.join(sorted(x)), dcp))
        count = defaultdict(list)
        for i in range(length):
            count[dcp[i]].append(strs[i])
        res = list(count.values())
        return res


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(strs))