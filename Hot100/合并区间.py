# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals.sort()
        length = len(intervals)
        if length <= 1:
            return intervals
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][0] == intervals[i + 1][0] and intervals[i][1] <= intervals[i + 1][1]:
                intervals.pop(i)
            elif intervals[i][1] >= intervals[i + 1][1]:
                intervals.pop(i + 1)
            elif intervals[i + 1][0] <= intervals[i][1] <= intervals[i + 1][1]:
                intervals[i + 1][0] = intervals[i][0]
                intervals.pop(i)
            else:
                i += 1

        return intervals

    def merge2(self, intervals: [[int]]) -> [[int]]:
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


if __name__ == '__main__':
    # ints = [[0, 1], [1, 3], [2, 6], [8, 10], [15, 18]]
    ints = [[1, 4], [2, 3]]
    s = Solution()
    print(s.merge(ints))