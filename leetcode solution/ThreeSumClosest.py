from typing import List


class ThreeSumClosest:
    def threeSumClosest(self,nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n):
            start = i + 1
            end = n - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if abs(target - sum) < abs(target - ans):
                    ans = sum
                if sum < target:
                    start += 1
                elif sum > target:
                    end -= 1
                else:
                    return sum
        return ans
