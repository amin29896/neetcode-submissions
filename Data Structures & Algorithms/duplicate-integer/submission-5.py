class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        
        for i in range(0,len(nums)):
            if(i==0):
                seen.add(nums[0])
                continue
            if(nums[i] in seen):
                return(True)
            else:
                seen.add(nums[i])

        return(False)       
