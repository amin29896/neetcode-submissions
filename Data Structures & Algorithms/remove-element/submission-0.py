class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        j=0
        aux=0
        for i in range(len(nums)):
            if (nums[i]!=val):
                k=k+1
                while(i>j):
                    if(nums[j]==val):
                        aux=nums[j]
                        nums[j]=nums[i]
                        nums[i]=aux
                        break
                    j=j+1
        return(k)

          
        
        