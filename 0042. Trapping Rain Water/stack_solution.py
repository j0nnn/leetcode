class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        current = 0
        stack = []

        for i in range(len(height)):
            # if the current height is less than the previous height or if the stack is empty, we simply append the index
            if not stack or height[stack[-1] < height[i]]:
                stack.append(i)
            else:
                # we pop from the stack until there is no more or the last height is greater than the current height
                while stack and height[stack[-1]] < height[i]:
                    popped = stack.pop()
                    if not stack:
                        break
                    else:
                        # horizontal distance
                        dist = i - stack[-1] - 1
                        # horizontal * min height = water
                        ans += dist * (min(height[i], height[stack[-1]]) - height[popped])
                stack.append(i)
        return ans