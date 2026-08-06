# ---------------
#    Method 01
# ---------------

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i

# ---------------
#    Method 02
# ---------------

# time complexity : O(n^2)
# space complexity : O(1)

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
