import collections
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # calculate occurence of each letter in string
        counter = collections.Counter(s)

        # put all characters in a maxHeap
        maxHeap = []
        for k,v in counter.items():
            heapq.heappush(maxHeap, [-v, k])
        
        result = ""
        while maxHeap:
            value, character = heapq.heappop(maxHeap)
            if result and character == result[-1] and len(maxHeap) == 0: # if this is the last available character and it is repeating, such a string is impossible to make
                return ""
            elif result and character == result[-1]: # if there are other options, we pop out the second option and use that instead
                secondValue, secondCharacter = heapq.heappop(maxHeap)
                result += secondCharacter
                secondValue += 1
                if secondValue != 0:
                    heapq.heappush(maxHeap, [secondValue, secondCharacter])
                heapq.heappush(maxHeap, [value, character])
            else: # use the current popped out character
                result += character
                value += 1
                if value != 0:
                    heapq.heappush(maxHeap, [value, character])
        return result
