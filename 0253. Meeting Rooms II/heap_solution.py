import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort intervals by start time to better utilize it
        intervals.sort()
        result = 0
        heap = []

        # iterate through all the intervals in order of starting time while keeping track of maximum length of heap at all time
        for interval in intervals:
            # push interval into heap if there is nothing in there
            if not heap:
                heapq.heappush(heap, interval[1])
                result = max(result, len(heap))
            else:
                # pop the interval with the earliest end time out of the heap
                earliest = heapq.heappop(heap)
                # if the start time is greater than the end time, we insert this interval into the heap instead
                if interval[0] >= earliest:
                    heapq.heappush(heap, interval[1])
                # or else, we push both of them back into the heap
                else:
                    heapq.heappush(heap, interval[1])
                    heapq.heappush(heap, earliest)
                # update maximum length of heap
                result = max(result, len(heap))
        return result