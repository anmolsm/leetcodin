class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
     hashSet = set()
     for index in nums:
       if index in hashSet:
         return True
       else:
          hashSet.add(index)
