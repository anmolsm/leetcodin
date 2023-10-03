class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberMap = {}
        length = len(nums)
        for i in range(length):
            complement = target - nums[i]
            if complement in numberMap:
                return [numberMap[complement], i]
            numberMap[nums[i]] = i

        return []
