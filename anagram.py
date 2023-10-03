class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashSet = defaultdict(int)

        for index in s:
            hashSet[index] += 1

        for index in t:
            hashSet[index] -=1

        for count in hashSet.values():
            if count != 0:
                return False
            
        return True
