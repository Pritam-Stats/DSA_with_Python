from typing import List, Optional, Dict, Tuple, Set

#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start

# ================================
# Author: Pritam
# ================================


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if not intervals:
            return []
        
        #sort bu st
        intervals.sort(key= lambda x: x[0])
        merged = [intervals[0]]

        for curr in intervals[1:]:
            prev_st, prev_end = merged[-1]
            curr_st, curr_end = curr

            if prev_end >= curr_st:
                merged[-1][1] = max(prev_end, curr_end)
            else:
                merged.append(curr)

        return merged


# @lc code=end


if __name__ == '__main__':
    sol = Solution()
    # Add your test cases here
