class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        leftMax, rightMax = 0, 0

        result = 0
        # end iteration when the two pointers converge
        while left < right:
            # move the pointer pointing to the shortest height, and update the max that the pointer has encountered and adding the water that the index traps to the running total
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                result += (leftMax - height[left])
                
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                result += (rightMax - height[right])
                
                right -= 1
        return result