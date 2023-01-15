from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # skip a value that has already been checked
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            if nums[i] > 0:
                break

            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr = nums[l] + nums[r]
                if curr == target:
                    # add the answer combination
                    res.append([nums[i], nums[l], nums[r]])
                if curr <= target:
                    # increment l until it points a different value
                    l += 1
                    while l < len(nums) and nums[l - 1] == nums[l]:
                        l += 1
                elif curr >= target:
                    # decrement r until it points a different value
                    r += -1
                    while r >= i and nums[r] == nums[r + 1]:
                        r += -1

        return res
