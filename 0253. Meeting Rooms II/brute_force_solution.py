import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort intervals by start time to better utilize it
        intervals.sort()
        result = 0
        stack = []

        # iterate through all the intervals in order of starting time while keeping track of maximum length of heap at all time
        for interval in intervals:
            # if stack is empty, append the interval to the stack
            if not stack:
                stack.append(interval)
            # iterate through all elements in the stack to see if there is an interval at ends before this one starts
            else:
                for i,s in enumerate(stack):
                    # if so, we pop said interval out and append this new interval
                    if s[1] <= interval[0]:
                        stack.pop(i)
                        stack.append(interval)
                        break
                # if none, we append this new interval
                else:
                    stack.append(interval)
            # update the maximum size achieved by the stack
            result = max(result, len(stack))
        return result
