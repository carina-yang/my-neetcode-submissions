class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = 0
        N = len(nums)

        while i < N:
            if nums[i] == val:
                for j in range(i + 1, N - count):
                    nums[j - 1] = nums[j]
                count += 1
                nums[N - count] = -1
            else:
                i += 1

        return N - count