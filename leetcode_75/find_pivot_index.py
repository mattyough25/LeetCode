'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
'''
'''
class Solution:
    def pivotIndex(self, nums: int) -> int:
        # Reverse Running Sum
        reverse_sum = list()
        nums_reverse = nums[::-1]
        for iNum2 in range(len(nums_reverse)):
            if iNum2 == 0:
                reverse_sum.append(nums_reverse[iNum2])
            else:
                reverse_sum.append(reverse_sum[-1] + nums_reverse[iNum2])
        
        # Running Sum
        if nums[0] == sum(nums):
            return 0
    
        running_sum = list()
        for iNum in range(len(nums)):
            if iNum == 0:
                running_sum.append(nums[iNum])
            else:
                running_sum.append(running_sum[-1] + nums[iNum])

            if running_sum[iNum] in reverse_sum and len(nums) - 1 > iNum + 1:
                #return iNum + 1
            
        print(running_sum)
        print(reverse_sum)
        return -1
'''

class Solution:
	def pivotIndex(self, nums: int) -> int:
		psums = [0]
		for i in range(len(nums)):
			# Notice i in psums is always one less than the current index
			psums.append(psums[i] + nums[i])

		for i in range(len(nums)):
			# Checking whether the left and the right are equal in area
			if psums[i] == psums[len(nums)] - psums[i+1]:
				return i

		return -1
# Test Cases

s = Solution()
nums = [1,7,3,6,5,6]
out = s.pivotIndex(nums)
print(out)

s = Solution()
nums = [1,2,3]
out = s.pivotIndex(nums)
print(out)

s = Solution()
nums = [2,1,-1]
out = s.pivotIndex(nums)
print(out)

s = Solution()
nums = [-1,-1,-1,-1,-1,-1]
out = s.pivotIndex(nums)
print(out)