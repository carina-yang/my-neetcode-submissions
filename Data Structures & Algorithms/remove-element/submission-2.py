class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        pointer = N - 1

        for i in range(N):
            while pointer >= 0 and nums[pointer] == val:
                nums[pointer] = -1
                pointer -= 1
                
            if nums[i] == val:
                nums[i] = nums[pointer]
                nums[pointer] = -1
                pointer -= 1
            
        return pointer + 1
