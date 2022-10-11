'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

class Solution:
    def twoSum(self, nums: int, target: int) -> int:
        for iNum in range(len(nums)):
            dif = target - nums[iNum]
            if dif in nums[iNum+1:]:
                new_nums = nums[iNum+1:]
                return [nums.index(nums[iNum]), new_nums.index(dif) + (iNum+1)]


# Test Cases
s1 = Solution()
nums1 = [2,7,11,15]
target1 = 9
out1 = s1.twoSum(nums1, target1)
print(out1)

s2 = Solution()
nums2 = [3,2,4]
target2 = 6
out2 = s2.twoSum(nums2, target2)
print(out2)

s3 = Solution()
nums3 = [3,3]
target3 = 6
out3 = s3.twoSum(nums3, target3)
print(out3)
