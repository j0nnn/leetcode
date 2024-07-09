class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        left = {} # keeps track of the nearest candle to the left of the plate
        right = {} # keeps track of the nearest candle to the right of the plate
        leftStar = [-1] * len(s) # keeps track of how many stars there are to the left

        # iterates through the string from the left
        # keeps track of plates on the left while also finding nearest candle on the left
        lastCandle = -1
        starCount = 0
        for i, c in enumerate(s): 
            if c == '*' and lastCandle != -1:
                left[i] = lastCandle
                starCount += 1
            elif c == '|':
                lastCandle = i
                left[i] = i
                leftStar[i] = starCount
            else:
                starCount += 1

        # keeps track of nearest candle on the right by iterating backwards
        lastCandle = -1
        for i in reversed(range(len(s))): 
            c = s[i]
            if c == '*' and lastCandle != -1:
                right[i] = lastCandle
            elif c == '|':
                lastCandle = i
                right[i] = i

        result = []
        for q in queries:
            # for each query, find the candles corresponding to the boundaries if they exist
            leftCandle = right[q[0]] if q[0] in right else -1
            rightCandle = left[q[1]] if q[1] in left else -1

            # if the boundary does not exist we return 0 else use the prefix sum of plates to find the number of plates in the boundary
            if leftCandle > rightCandle or leftCandle == -1 or rightCandle == -1: result.append(0)
            else: result.append(leftStar[rightCandle] - leftStar[leftCandle])
        return result

        
        