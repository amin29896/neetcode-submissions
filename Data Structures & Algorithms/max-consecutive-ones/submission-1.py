class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sm=0
        s=0
        for i in range(len(nums)):
            if nums[i]==1:
                s=s+1
            else:
                s=0
            if(s>sm):
                sm=s
        return(sm)



        