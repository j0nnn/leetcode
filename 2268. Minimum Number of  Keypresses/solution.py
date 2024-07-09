import collections
import heapq

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = collections.Counter(s)
        maxHeap = []
        for k,v in counter.items():
            heapq.heappush(maxHeap, [-v, k])
        
        count = 1
        result = 0
        while maxHeap:
            for i in range(9):
                if not maxHeap: break
                occurence, letter = heapq.heappop(maxHeap)
                result += occurence * -1 * count
            count += 1
        return result