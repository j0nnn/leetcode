import collections
import heapq

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        # count the number of occurences for each letter
        counter = collections.Counter(s)

        # parse them all into a maxHeap
        maxHeap = []
        for k,v in counter.items():
            heapq.heappush(maxHeap, [-v, k])
        
        count = 1
        result = 0
        while maxHeap:
            for i in range(9): # count to see if we have exceeded the number of mapped keypresses
                if not maxHeap: break
                occurence, letter = heapq.heappop(maxHeap)
                result += occurence * -1 * count
            count += 1
        return result