class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                width = i - idx
                max_area = max(max_area, height * width)
                start = idx
            
            stack.append((start, h))
        
        for idx, height in stack:
            width = len(heights) - idx
            max_area = max(max_area, height * width)
        
        return max_area