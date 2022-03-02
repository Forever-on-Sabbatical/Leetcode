class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i, j in enumerate(nums):
            temp=(target - j)            
            if temp in nums:
                if i != nums.index(temp):
                    res.append(i)
                    res.append(nums.index(temp))
                    return res
        return res
                        