class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        curr_max = arr[N - 1]
        arr[N - 1] = -1
        
        for i in range(N - 2, -1, -1):
            tmp = arr[i]
            arr[i] = curr_max
            curr_max = max(curr_max, tmp)
        
        return arr
