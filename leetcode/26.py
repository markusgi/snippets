#26. Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        i = 1
        while (i < len(nums)):
            if nums[i] == nums[i-1]:
                nums.pop(i)
                count += 1
            else:
                i += 1
        return len(nums)


nums = [1,1,2,2,2,2,3,4,5,6,6]
print(Solution.removeDuplicates(1,nums))