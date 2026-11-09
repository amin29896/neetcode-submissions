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
                
        
        
        
        i=1
        while(i<len(nums)and i>=1):
            for j in range(0,i):
                if(nums[j]==nums[i]):
                    return(True)
            i=i+1
        return(False)
        
        
        