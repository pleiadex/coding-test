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

                if nums[l] < nums[mid]:
                    l = mid + 1
                elif nums[l] > nums[mid]:
                    r = mid - 1
                else:
                    return min(res, nums[l], nums[r])
        return res