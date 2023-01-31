from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                return min(res, nums[l])
            else:
                mid = (l + r) // 2
                res = min(res, nums[mid])

                # better to compare to nums[r] since l equals to mid when the length is two.
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return res